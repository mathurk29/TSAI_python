import inspect
import random
from decimal import *
import math
import re
from warnings import resetwarnings

import test_session4 as tm


class Qualean:

    '''
    Accepts one of the three possible states - Truth/False/Maybe and multiplies it with randomly generated number between -1 to 1 and stores that internally.
    Several dunder methods are defined for various Numerical operations on the number.
    '''

    def __init__(self, number=random.choice([1, 0, -1])):
        if number not in [1, 0, -1]:
            raise ValueError('The number should be [1,0,-1]')
        self.truth_val = True
        if number == 0:
            self.truth_val = False

        self.number = round(number * random.uniform(-1, 1), 10)

    # defining object representation
    def __repr__(self):
        return 'Qualean Class Instance'

    # defining string representation

    def __str__(self):
        return 'Qualean String for number: ' + str(self.number)

    # retuns THE number

    def return_qualean(self):
        return self.number

    def __sqrt__(self):
        if self.number >= 0:
            return round(Decimal(math.sqrt(self.number)), 10)
        else:
            return str(round(Decimal(math.sqrt(self.__invertsign__())),  10)) + 'i'

    def __invertsign__(self):
        return (-1) * self.number

    def __float__(self):
        return float(self.number)

    def __add__(self, q2):
        if not (isinstance(q2, float) or isinstance(q2, Qualean)):
            raise TypeError()
        if isinstance(q2, Qualean):
            return self.number + q2.return_qualean()
        elif isinstance(q2, float):
            return self.number + q2

    def __mul__(self, q2):
        if not (isinstance(q2, float) or isinstance(q2, Qualean)):
            raise TypeError()
        if isinstance(q2, Qualean):
            return self.number * q2.return_qualean()
        elif isinstance(q2, float):
            return self.number * q2

    # greater than or equals to

    def __ge__(self, q2):
        if not (isinstance(q2, float) or isinstance(q2, Qualean)):
            raise TypeError()
        if isinstance(q2, Qualean):
            return self.number >= q2.return_qualean()
        elif isinstance(q2, float):
            return self.number >= q2

    # greater than
    def __gt__(self, q2):
        if not (isinstance(q2, float) or isinstance(q2, Qualean)):
            raise TypeError()
        if isinstance(q2, Qualean):
            return self.number > q2.return_qualean()
        elif isinstance(q2, float):
            return self.number > q2

    # lesser than or equals to

    def __le__(self, q2):
        if not (isinstance(q2, float) or isinstance(q2, Qualean)):
            raise TypeError()
        if isinstance(q2, Qualean):
            return self.number <= q2.return_qualean()
        elif isinstance(q2, float):
            return self.number <= q2

    # lesser than
    def __lt__(self, q2):
        if not (isinstance(q2, float) or isinstance(q2, Qualean)):
            raise TypeError()
        if isinstance(q2, Qualean):
            return self.number < q2.return_qualean()
        elif isinstance(q2, float):
            return self.number < q2

    def __eq__(self, q2):
        if not (isinstance(q2, float) or isinstance(q2, Qualean)):
            raise TypeError()
        if isinstance(q2, Qualean):
            return self.number == q2.return_qualean()
        elif isinstance(q2, float):
            return self.number == q2

    def __bool__(self):
        return bool(self.return_qualean())

    def __and__(self, q2):
        if q2 is None:
            return False
        if self.truth_val == False:  # q1
            return False
        else:
            return q2.truth_val

    def __or__(self, q2):
        if self.truth_val:
            return self.truth_val
        else:
            if q2 is None:
                return True
            else:
                return self.truth_val
