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
