# -*- coding: utf-8 -*-
__author__= 'bartosz_koperek'

import logging
from config import configfile
from page_base import BasePage
import exceptions
from selenium.common.exceptions import TimeoutException

class ChooseFlight(BasePage):
    SPAN_PRICE_FLIGHT_XPATH_LOCATOR = '//span[@ng-hide="!flight.fare"]'
    SPAN_SOLDOUT_XPATH_LOCATOR = '//span[@translate="trips.flight_list_table.soldout"]'
    BUTTON_CONTINUE_XPATH_LOCATOR = '//button[@translate="trips.summary.buttons.btn_continue"]'
    CHOOSE_FLIGHT_LIST_XPATH_LOCATOR = '//div[@model="outboundFlightListModel"]'

    def __init__(self,driver):
        self.driver = driver
        logging.debug('Current url = {}'.format(self.driver.current_url))
        self.url = driver.current_url
        logging.debug('New object of class {} constructed'.format(self.__class__.__name__))

    def check_webpage(self):
        self.check_if_page_is_loaded('xpath',self.CHOOSE_FLIGHT_LIST_XPATH_LOCATOR)

    def click_first_flight(self):
        logging.info('Choosing flight.')
        self.click_and_wait(self.SPAN_PRICE_FLIGHT_XPATH_LOCATOR,'xpath')

    def check_if_flights_are_soldout(self):
        logging.info('Checking if any flight is available.')
        try:
            if self.find_element('xpath',self.SPAN_SOLDOUT_XPATH_LOCATOR,timeout=configfile.timeout_soldout_msg):
                raise exceptions.FlightsSoldOutError('Flights are sold out!')
            else:
                logging.info('Flight found.')
        except TimeoutException,exceptions.ElementNotFound:
            pass

    def click_continue(self):
        logging.info('Clicking continue button.')
        self.click_element(self.BUTTON_CONTINUE_XPATH_LOCATOR,'xpath')