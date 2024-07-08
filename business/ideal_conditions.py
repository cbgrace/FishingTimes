"""
This module will contain methods to calculate the ideal fishing times for the next 2 weeks

The criteria are somewhat a work in progress, but here is what I am thinking:

- During daylight hours (obviously) calculated using sunrise & sunset times for that day.
- Temp between 65 & 90 degrees (this is my preference, in future iterations should let the user decide)
- Prime conditions = overcast, >2 hours before or after rain
- Good conditions = overcast
- Obviously no rain
"""