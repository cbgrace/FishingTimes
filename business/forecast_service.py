import dal
from datetime import date, timedelta
from exceptions import BusinessLogicException, DalException
from logging_config import get_logger


logger = get_logger(__name__)
TODAYS_DATE = date.today()
TWO_WEEKS_LATER = TODAYS_DATE + timedelta(days=13)

def get_forecast_data(latitude, longitude):
    try:
        logger.info('retrieving forecast data')
        response = dal.retrieve_forecast(latitude, longitude, TODAYS_DATE, TWO_WEEKS_LATER)
        return response
    except (DalException, Exception):
        logger.error('Unable to gather forecast data')
        raise BusinessLogicException


def get_lat_long(address: str):
    """
    calls on the get_lat_long function in the dal to return a latitude and longitude from Open Street Maps for a
        given address.
    :param address: the user's address they enter into the gui form
    :return: the results of dal.get_lat_long()
    """
    try:
        return dal.get_lat_long(address.strip())
    except DalException:
        logger.error('unable to get lat & long from open street maps')
        raise BusinessLogicException