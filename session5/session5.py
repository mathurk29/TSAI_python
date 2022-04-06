"""Assignment 5: time_it function and other serveral functions to illusttrate the working of Functional Arguments."""

from math import e, remainder, sqrt
import math
import re
from sys import flags
import time

def time_it(fn, *args, repetitions=1, **kwargs):
    """This is a genralized function to call any function
    user specified number of times and return the average
    time taken for calls"""

    # Repetition should be positive number
    l = []
    for _ in range(repetitions):
        start = time.perf_counter()
        fn(*args, **kwargs)
        end = time.perf_counter()
        l.append(end - start)
    if len(l) == 0:
        return 0
    else:
        return float(sum(l)/len(l))


def squared_power_list(number: int, *args , start=0, end=5, **kwargs) -> list:
    """Returns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""

    # Validations "if" block
    if type(number) is not int:
        raise TypeError("Only integer type arguments are allowed")

    if start < 0 or end < 0:
        raise ValueError("The Value of start or end can't be negative.")
    if start > end:
        raise ValueError("Value of start should be less than end")
    if number >= 10:
        raise ValueError("Value of number should be less than 10")
    if len(args):
        raise TypeError('takes maximum 1 positional arguments')
    if len(kwargs):
        raise TypeError('maximum 2 keyword/named arguments')

    # Return the list of number to the power of numbers from start to end
    #print([number**x for x in range(start, end)])
    return [number**x for x in range(start, end)]


def polygon_area(length: int, *args, sides=3, **kwargs)-> float: 
    """Returns area of a regular polygon with number of sides between
    3 to 6 bith inclusive"""

    # Validations
    if type(length) is not int:
        raise TypeError('Only integer type arguments are allowed for length')
    if type(sides) is not int:
        raise TypeError('Only integer type arguments are allowed for sides')
    if sides < 3 or sides > 6:
        raise ValueError('sides should be between 3 to 6 both inclusive')
    if len(args):
        raise TypeError(
            'polygon_area function takes maximum 1 positional arguments, more provided')
    if len(kwargs):
        raise TypeError(
            'polygon_area function take maximum 1 keyword/named arguments, more provided')

    # Return area
    if sides == 3:
        return ((length ** 2) * math.sqrt(3)) / 4
    if sides == 4:
        return length ** 2
    if sides == 5:
        return (sqrt(5 * (5 + 2 * (sqrt(5)))) * length * length) / 4
    if sides == 6:
        return (((3 * math.sqrt(3)) / 2) * (length ** 2))


def temp_converter(temp: int, *args, temp_given_in='f', **kwargs) -> float:
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""

    # Validations
    if type(temp) is not int:
        raise TypeError('Only integer type arguments are allowed')
    if type(temp_given_in) is not str:
        raise TypeError('Charcater string expected')
    if temp_given_in not in ('f', 'c', 'F', 'C'):
        raise ValueError('Only f or c is allowed')
    if (temp_given_in in ('c', 'C') and temp < -273.15):
        raise ValueError(
            "Temprature can't go below -273.15 celsius = 0 Kelvin")
    if (temp_given_in in ('f', 'F') and temp < -273.15):
        raise ValueError(
            "Temprature can't go below -459.67 fahrenheit = 0 Kelvin")
    if len(args):
        raise TypeError(
            'temp_converter function takes maximum 1 positional arguments, more provided')
    if len(kwargs):
        raise TypeError(
            'temp_converter function take maximum 1 keyword/named arguments, more provided')

    # Return the converted temprature
    if temp_given_in in ('f', 'F'):
        return (temp - 32) / 1.8
    else:
        return (temp * 1.8) + 32


def speed_converter(speed: int, *args, dist='km', time='min', **kwargs) -> float:
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day """

    # Validations
    if len(args):
        raise TypeError(
            'speed_converter function takes maximum 1 positional arguments, more provided')
    if len(kwargs):
        raise TypeError(
            'speed_converter function take maximum 2 keyword/named arguments, more provided')
    if type(speed) not in (int, float):
        raise TypeError('Speed can be int or float type only')
    if type(dist) is not str:
        raise TypeError('Charcater string expected for distance unit')
    if type(time) is not str:
        raise TypeError('Charcater string expected for time')
    if speed < 0:
        raise ValueError("Speed can't be negative")
    if speed > 300000:
        raise ValueError("Speed can't be greater than speed of light")
    if time.lower() not in ('ms', 's', 'min', 'hr', 'day'):
        raise ValueError(
            'Incorrect unit of Time. Only ms/s/min/hr/day allowed')
    if dist.lower() not in ('km', 'm', 'ft', 'yrd'):
        raise ValueError(
            'Incorrect unit of distance. Only km/m/ft/yrd allowed')

    # convert numberator
    result = speed
    time = time.lower()
    dist = dist.lower()
    if dist == 'km':
        pass
    elif dist == 'm':
        result *= 1000
    elif dist == 'ft':
        result *= 3280.8375
    elif dist == 'yrd':
        result *= 1093.609

    # convert denominator
    if time == 'day':
        result *= 24
    elif time == 'hr':
        pass
    elif time == 'min':
        result /= 60
    elif time == 's':
        result /= (60 * 60)
    elif time == 'ms':
        result /= (60 * 60 * 1000)
    #print(f'before rounding {result}')
    return round(result)
