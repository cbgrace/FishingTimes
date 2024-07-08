import dal
from datetime import date, timedelta
from exceptions import BusinessLogicException, DalException
from logging_config import get_logger
import models


logger = get_logger(__name__)
TODAYS_DATE = date.today()
TWO_WEEKS_LATER = TODAYS_DATE + timedelta(days=14)


def get_forecast_data(latitude, longitude):
    """
    I commandeered this from a previous project. It could probably use some optimization...
    :param latitude: the user's latitude
    :param longitude: the user's longitude
    :return: a list of Forecast objects.
    """
    try:
        logger.info('attempting to get forecast data')
        # get forecast data from the dal
        response = dal.retrieve_forecast(latitude, longitude, TODAYS_DATE, TWO_WEEKS_LATER)
        relevant_data = []
        i = 0
        # grab the timezone offset from the forecast data, because it is not contained in the same level of the json
        # as the other data.
        timezone = response['tzoffset']
        # then go through each day in the response and grab all other needed data.
        for day in response['days']:
            forecast_date = day['datetime']
            sunrise = day['sunrise']
            sunset = day['sunset']
            moonphase = day['moonphase']
            # I ran into an error where the moonset was not included one day...
            if 'moonrise' in day:
                moonrise = day['moonrise']
            else:
                moonrise = 0
            if 'moonset' in day:
                moonset = day['moonset']
            else:
                moonset = 0
            hour_and_conditions_dict = {}
            for hour in response['days'][i]['hours']:
                hour_and_conditions_dict[hour['datetime']] = (hour['temp'], hour['conditions'], hour['pressure'])
            i += 1
            # create a Forecast object with the data
            new_forecast = models.Forecast(forecast_date, sunrise, sunset, moonphase, moonrise, moonset, timezone,
                                           hour_and_conditions_dict)
            # append it to my list to be returned.
            relevant_data.append(new_forecast)
        logger.info('Successfully gathered relevant forecast data.')
        return relevant_data
    except (DalException, Exception):
        logger.error('Unable to gather forecast data...')
        raise BusinessLogicException


def get_lat_long(address: str):
    """
    calls on the get_lat_long function in the dal to return a latitude and longitude from Open Street Maps for a
        given address.
    :param address: the user's address they enter into the gui form
    :return: the results of dal.get_lat_long()
    """
    try:
        logger.info("Retrieving user's lat/lon from their address string.")
        return dal.get_lat_long(address)  # already .strip()'d
    except DalException:
        logger.error('unable to get lat & long from open street maps')
        raise BusinessLogicException