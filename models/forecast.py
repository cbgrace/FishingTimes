from datetime import datetime, timedelta

"""
This module contains a class which models a Forecast for a given day

Methods:
--------
    translate_moonphase(self):
        translates the moonphase number into a more human-readable string (e.g. 0.50 = full)    
    The only other methods are __init__, __str__, and properties...

Constants:
----------
    NOON: represents noon as a datetime.time object. 
"""

NOON = datetime.strptime("12:00:00", "%H:%M:%S").time()


class Forecast:
    def __init__(self, date, sunrise, sunset, moonphase, moonrise, moonset, timezone_offset, hourly_conditions_dict):
        self._date = date
        self._sunrise = sunrise
        self._sunset = sunset
        self._moonphase = float(moonphase)
        self._moonrise = moonrise
        self._moonset = moonset
        self._timezone_offset = float(timezone_offset)
        self._hourly_conditions_dict = hourly_conditions_dict

    """
    Right now the pressure is in the hourly_conditions_dict, it changes by the hour and I need to know the pressure for
    each hour, so it makes sense to keep it there at the moment. 
    
    To convert from mb (the unit of pressure this weather data is stated in) to inHg (the unit I have for optimal
    fishing conditions) you divide the pressure value by 33.864
    
    ideal barometric pressure: 29.8 to 30.2 inHg , or 1009.144 -> 1022.69 mb
    """

    @property
    def date(self):
        return self._date

    @property
    def sunrise(self):
        return self._sunrise

    @property
    def sunset(self):
        return self._sunset

    @property
    def moonphase(self):
        return self._moonphase

    @property
    def moonrise(self):
        # sometimes the api does not return a moonrise, so I must check for that.
        if self._moonrise != 0:
            # attach the Forecast date to the moonrise time
            return f'{self._date} {self._moonrise}'
        else:
            return self._moonrise

    @property
    def moonset(self):
        if self._moonset != 0:
            # add self._date & convert it to datetime so I can use operators...
            moonset_time = f'{self._date} {self._moonset}'
            moonset_time_dtobj = datetime.strptime(moonset_time, "%Y-%m-%d %H:%M:%S")
            if self._moonrise != 0:
                # convert moonrise to a datetime object as well
                moonrise_time_dtobj = datetime.strptime(self.moonrise, "%Y-%m-%d %H:%M:%S")
                if moonrise_time_dtobj > moonset_time_dtobj:
                    # then the moonset is the next day... so add one day to the datetime
                    moonset_time_dtobj += timedelta(days=1)
                    return datetime.strftime(moonset_time_dtobj, "%Y-%m-%d %H:%M:%S")
                else:
                    return datetime.strftime(moonset_time_dtobj, "%Y-%m-%d %H:%M:%S")
            else:
                return datetime.strftime(moonset_time_dtobj, "%Y-%m-%d %H:%M:%S")
        else:
            return self._moonset

    @property
    def timezone_offset(self):
        return self._timezone_offset

    @property
    def hourly_conditions_dict(self):
        return self._hourly_conditions_dict

    def translate_moonphase(self):
        """
        translates the moon phase into a more human-readable string
        :return: a string representing the current moonphase for this Forecast.
        """
        if self._moonphase == 0:
            return 'New Moon'
        elif self._moonphase < 0.25:
            return 'Waxing Crescent'
        elif self._moonphase == 0.25:
            return 'First Quarter'
        elif self._moonphase < 0.5:
            return 'Waxing Gibbous'
        elif self._moonphase == 0.5:
            return 'Full'
        elif self._moonphase < 0.75:
            return 'Waning Gibbous'
        elif self._moonphase == 0.75:
            return 'Last Quarter'
        elif self._moonphase < 1:
            return 'Waning Crescent'
        else:
            return 'Error Grabbing Moon Phase'  # just in case...

    def return_hourly_pressure(self):
        hourly_pressure_dict = {}  # create a dict to store the hourly pressures
        for hour, forecast_tuple in self._hourly_conditions_dict.items():
            hourly_pressure_dict[hour] = forecast_tuple[2]  # set it equal to the second item in the tuple (the pressure)
        return hourly_pressure_dict

    def return_hourly_conditions(self):
        # I guess I might as well add this too, if I add the above method.
        hourly_conditions_dict = {}  # create a dict to store the hourly condition strings
        for hour, forecast_tuple in self._hourly_conditions_dict.items():
            hourly_conditions_dict[hour] = forecast_tuple[1]  # set it equal to the first item in the tuple
        return hourly_conditions_dict

    def return_hourly_temps(self):
        hourly_temps_dict = {}
        for hour, forecast_tuple in self._hourly_conditions_dict.items():
            hourly_temps_dict[hour] = forecast_tuple[0]
        return hourly_temps_dict

    def __str__(self):
        return f"{self.date} rise:{self.sunrise}, sets:{self.sunset}, moon:{self.translate_moonphase()}{self._moonset}, {self._hourly_conditions_dict}"

    def __repr__(self):
        # repr is necessary for printing objects to the console (I usually only come across this in testing)
        return f"{self.date} rise:{self.sunrise}, sets:{self.sunset}, moon:{self.translate_moonphase()} {self._moonset}, {self._hourly_conditions_dict}"

