import requests
from exceptions import DalException
from logging_config import get_logger


logger = get_logger(__name__)
GOOD_RESPONSE_CODE = 200


def get_lat_long(address: str) -> tuple:
    """
    gets latitude and longitude for a given address from Open Street Maps api.
    :param address: user's address they entered into the gui
    :return: latitude and longitude for the user, in the form of a tuple.
    """
    url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'format': 'json',
        'q': address
    }
    headers = { 'user-agent': 'FishingTimes by Charles Grace' }  # have to include identifying user-agent with OpenStreetMaps now...
    logger.info('grabbing latitude and longitude from openstreetmap')
    coords_response = requests.get(url, params=params, headers=headers)
    print(coords_response.status_code)
    if coords_response.status_code == GOOD_RESPONSE_CODE:
        coords_response = coords_response.json()
        try:
            lat_long = (coords_response[0]['lat'], coords_response[0]['lon'])
            return lat_long
        except Exception:
            logger.error(f'unable to get coords for address {address}')
            raise DalException
    else:
        logger.error(f'unable to get coords for address {address}, bad response code')
        raise DalException


def retrieve_forecast(latitude, longitude, start_date, end_date):
    """
    gets hourly forecast data for given dates and location from VisualCrossing api.
    :param latitude: the user's latitude
    :param longitude: the user's longitude
    :param start_date: the start date you would like to forecast
    :param end_date: the last day you want the forecast for
    :return: weather data from VisualCrossing in JSON format
    """
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{latitude},{longitude}/{start_date}/{end_date}"
    params = {
        'key': '7VGGR8GZQBVWFMPQ276TFHMKM',
        'elements': "datetime,moonphase,sunrise,sunset,moonrise,moonset,conditions,pressure"
    }
    logger.info('attempting to get sunrise/sunset times from visualcrossing')
    response = requests.get(url, params=params)
    if response.status_code == GOOD_RESPONSE_CODE:
        response = response.json()
        if response:
            logger.info('succesffuly retireved sunrise/sunset times')
            return response
        else:
            logger.error('unable to retrieve sunrise/sunset times')
            raise DalException
    else:
        logger.error('unable to retrieve sunrise/sunset times, bad response code')
        raise DalException