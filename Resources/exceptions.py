# -*- coding: utf-8 -*-
__author__= 'bartosz_koperek'

class PaymentDeclinedNotFoundError(Exception):
    pass

class NoFlightsForThisDateError(Exception):
    pass

class FlightsSoldOutError(Exception):
    pass

class PageNotLoadedError(Exception):
    pass

class ElementNotFoundError(Exception):
    pass

class InvalidCreditCardNumberError(Exception):
    pass