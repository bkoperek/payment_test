# -*- coding: utf-8 -*-
__author__= 'bartosz_koperek'

import logging
from page_base import BasePage

class GoToCheckout(BasePage):
    POPUP_XPATH_LOCATOR = '//core-icon[@icon-id="icons.glyphs.close"]'
    BUTTON_CHECKOUT_XPATH_LOCATOR = '//button[@class="core-btn-primary core-btn-block core-btn-medium ng-scope"]'

    def __init__(self,driver):
        self.driver = driver
        logging.debug('New object of class {} constructed'.format(self.__class__.__name__))

    def check_webpage(self):
        self.check_if_page_is_loaded('xpath',self.BUTTON_CHECKOUT_XPATH_LOCATOR)

    def close_popup(self):
        logging.info('Closing reserve seat popup.')
        try:
            self.click_and_wait(self.POPUP_XPATH_LOCATOR,'xpath')
        except:
            logging.debug('Popup prompt not appeared.')

    def click_checkout_button(self):
        logging.info('Clicking checkout button.')
        self.click_and_wait(self.BUTTON_CHECKOUT_XPATH_LOCATOR,'xpath')
