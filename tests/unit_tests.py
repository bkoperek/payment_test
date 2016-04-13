# -*- coding: utf-8 -*-
__author__= 'bartosz_koperek'

import unittest
import time
from selenium import webdriver
from Resources.base_page import BasePage
from Resources.home_page import HomePage
from Resources.choose_flight import ChooseFlight
from Resources.go_to_checkout import GoToCheckout
from Resources.payment import Payment

class TestInterface(unittest.TestCase):
    def setUp(self):
        self.url = 'https://www.ryanair.com/ie/en/'
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

    def test_someone_can_1_provide_flight_details(self):
        self.home_page = HomePage(self.driver,self.url)
        self.home_page.check_webpage()
        self.home_page.choose_one_way_flight()
        self.home_page.fill_flight_from()
        self.home_page.fill_flight_to()
        self.home_page.click_continue()
        self.home_page.fill_date()
        self.home_page.expand_passengers()
        self.home_page.set_passengers()
        self.home_page.click_letsgo()

    # def test_someone_can_2_choose_flight(self):
    #     time.sleep(4)
    #     self.choose_flight = ChooseFlight(self.driver)
    #     self.choose_flight.click_first_flight()
    #
    # def test_someone_can_3_go_to_checkout(self):
    #     self.go_to_checkout = GoToCheckout(self.driver)
    #     time.sleep(3)
    #     self.go_to_checkout.close_popup()
    #     time.sleep(1)
    #     self.go_to_checkout.click_checkout_button()
    #
    # def test_someone_can_4_provide_payment_details(self):
    #     self.payment_page = Payment(self.driver)
    #     time.sleep(3)
    #     self.payment_page.fill_in_payment_and_contact_details()

    def tearDown(self):
        #self.driver.close()
        pass

if __name__ == '__main__':
    unittest.main()