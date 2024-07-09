"""
This module will contain methods to calculate the ideal fishing times for the next 2 weeks

The criteria are somewhat a work in progress, but here is what I am thinking:

- During daylight hours (obviously) calculated using sunrise & sunset times for that day.
- Temp between 65 & 90 degrees (this is my preference, in future iterations should let the user decide)
- Prime conditions = overcast, >2 hours before or after rain
- Good conditions = overcast
- Obviously no rain
"""
from models import Forecast


def sort_forecast_list(forecast_list: [Forecast]) -> []:
    """
    Hopefully this method will sort a list of Forecast data and return dates & times that match my ideal criteria
    :param forecast_list:
    :return:
    """
    # so I need to take the list, and look for 2 hours of 'not rain' before (at least) an hour of rain
    # result_dict = {}
    # rain_keys = [k for k, v in weather_dict.items() if v == 'rain']
    #
    # for key in rain_keys:
    #     for offset in range(-2, 3):  # range from -2 to 2
    #         check_key = key + offset
    #         if check_key in weather_dict and check_key not in result_dict:
    #             result_dict[check_key] = weather_dict[check_key]
    #
    # print(result_dict)