# -*- coding: utf-8 -*-
__author__= 'bartosz_koperek'

import exceptions
from config import configfile
import logging, exceptions
from page_base import BasePage
from selenium.common.exceptions import TimeoutException

class HomePage(BasePage):
    INPUT_ONEWAY_ID_LOCATOR = 'flight-search-type-option-one-way'
    INPUT_FLIGHT_FROM_XPATH_LOCATOR = '//input[@placeholder="Departure airport"]'
    INPUT_FLIGHT_TO_XPATH_LOCATOR = '//input[@placeholder="Destination airport"]'
    INPUT_DAY_XPATH_LOCATOR = '//input[@placeholder="DD"]'
    INPUT_MONTH_XPATH_LOCATOR = '//input[@placeholder="MM"]'
    INPUT_YEAR_XPATH_LOCATOR = '//input[@placeholder="YYYY"]'
    INPUT_ADULTS_XPATH_LOCATOR = '//input[@aria-label="Adults 16+ years"]'
    INPUT_TEENS_XPATH_LOCATOR = '//input[@aria-label="Teens 12-15 years"]'
    INPUT_CHILDRENS_XPATH_LOCATOR = '//input[@aria-label="Children 2-11 years"]'
    INPUT_INFANTS_XPATH_LOCATOR = '//input[@aria-label="Infants Under 2 years"]'
    RYANAR_ICON_ID_XPATH_LOCATOR = '//core-icon[@icon-id="icons.common.ryanair-logo"]'
    BUTTON_CONTINUE_XPATH_LOCATOR = '//span[@translate="common.buttons.continue"]'
    BUTTON_LETSGO_XPATH_LOCATOR = '//span[@translate="common.buttons.lets_go"]'
    SPAN_NO_FLIGHTS_XPATH_LOCATOR = '//span[@translate="foh.home.flight_search_errors.no_flights_available_for_this_date"]'
    DROPDOWN_PASSENGERS_XPATH_LOCATOR = '//div[@class="col-passengers ng-isolate-scope"]/div/div/div/div' \
                                                 '[@class="dropdown-handle"]/core-icon[@icon-type="svg-symbol"]'

    def __init__(self,driver,url):
        logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s",level=logging.DEBUG)
        logging.debug('New object of class {} constructed'.format(self.__class__.__name__))
        self.driver = driver
        self.url = url

    def check_webpage(self):
        self.check_if_page_is_loaded('xpath',self.RYANAR_ICON_ID_XPATH_LOCATOR)

    def choose_one_way_flight(self):
        logging.info('Choosing one way flight.')
        self.click_element(self.INPUT_ONEWAY_ID_LOCATOR,'id')

    def fill_flight_from(self,flight_from):
        logging.info('Entering flight from.')
        self.fill_element_by_text_and_send_tab(self.INPUT_FLIGHT_FROM_XPATH_LOCATOR,'xpath',flight_from)

    def fill_flight_to(self,flight_to):
        logging.info('Entering flight to.')
        self.fill_element_by_text_and_send_tab(self.INPUT_FLIGHT_TO_XPATH_LOCATOR,'xpath',flight_to)

    def click_continue(self):
        logging.info('Clicking continue.')
        self.click_element(self.BUTTON_CONTINUE_XPATH_LOCATOR,'xpath')

    def click_letsgo(self):
        logging.info('Clicking lets go.')
        self.click_element(self.BUTTON_LETSGO_XPATH_LOCATOR,'xpath')

    def fill_date(self,date):
        logging.info('Entering flight date.')
        self.fill_element_by_text(self.INPUT_DAY_XPATH_LOCATOR,'xpath',date[0])
        self.fill_element_by_text(self.INPUT_MONTH_XPATH_LOCATOR,'xpath',date[1])
        self.fill_element_by_text(self.INPUT_YEAR_XPATH_LOCATOR,'xpath',date[2])

    def check_if_no_flights_message_appeared(self):
        logging.info('Checking if any flight is available on chosen date.')
        try:
            if self.find_element('xpath',self.SPAN_NO_FLIGHTS_XPATH_LOCATOR,timeout=configfile.timeout_no_flight_msg):
                raise exceptions.NoFlightsForThisDateError('There are no flights for this date!')
            else:
                logging.info('Date is OK.')
        except TimeoutException, exceptions.ElementNotFoundError:
            pass

    def expand_passengers(self):
        logging.info('Opening passengers dropdown list.')
        self.click_element(self.DROPDOWN_PASSENGERS_XPATH_LOCATOR,'xpath')

    def set_passengers(self,adults,teens,childrens=0,infants=0):
        logging.info('Entering passengers.')
        self.fill_element_by_text(self.INPUT_ADULTS_XPATH_LOCATOR,'xpath',adults)
        self.fill_element_by_text(self.INPUT_TEENS_XPATH_LOCATOR,'xpath',teens)
        self.fill_element_by_text(self.INPUT_CHILDRENS_XPATH_LOCATOR,'xpath',childrens)
        self.fill_element_by_text(self.INPUT_INFANTS_XPATH_LOCATOR,'xpath',infants)