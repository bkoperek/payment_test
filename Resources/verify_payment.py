# -*- coding: utf-8 -*-
__author__= 'bartosz_koperek'

from decorator_control import fun_call_decorator
from config import configfile
import logging
from selenium import webdriver
from Resources.page_home import HomePage
from Resources.page_choose_flight import ChooseFlight
from Resources.page_go_to_checkout import GoToCheckout
from Resources.page_payment import Payment
import exceptions

class PaymentVerifier():
    def __init__(self):
        logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s",level=logging.DEBUG)
        self.url = configfile.url

    @fun_call_decorator
    def initialize_browser(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    @fun_call_decorator
    def fill_in_flight_details(self,flight_from,flight_to,flight_date, adults_number, children_number):
        flight_date = flight_date.split('/')
        self.initialize_browser()
        self.driver.get(self.url)
        self.home_page = HomePage(self.driver,self.url)
        self.home_page.check_webpage()
        self.home_page.choose_one_way_flight()
        self.home_page.fill_flight_from(flight_from)
        self.home_page.fill_flight_to(flight_to)
        self.home_page.fill_date(flight_date)
        self.home_page.check_if_no_flights_message_appeared()
        self.home_page.expand_passengers()
        self.home_page.set_passengers(adults_number,children_number)
        self.home_page.click_letsgo()
        self.choose_flight()
        self.go_to_checkout()

    @fun_call_decorator
    def choose_flight(self):
        self.choose_flight = ChooseFlight(self.driver)
        self.choose_flight.check_webpage()
        self.choose_flight.click_first_flight()
        self.choose_flight.click_continue()

    @fun_call_decorator
    def go_to_checkout(self):
        self.go_to_checkout = GoToCheckout(self.driver)
        self.go_to_checkout.close_popup()
        self.go_to_checkout.click_checkout_button()

    @fun_call_decorator
    def provide_payment_details(self,credit_card_number,credit_card_exp_date,credit_card_cvv):
        credit_card_exp_date = credit_card_exp_date.split('/')
        self.payment_page = Payment(self.driver)
        self.payment_page.check_webpage()
        self.payment_page.generate_passengers()
        self.payment_page.choose_titles(configfile.default_title)
        self.payment_page.input_email(configfile.default_email)
        self.payment_page.select_country(configfile.default_country)
        self.payment_page.input_phone_number(configfile.default_phone_number)
        self.payment_page.input_card_number(credit_card_number)
        self.payment_page.select_card_type(configfile.default_card_type)
        self.payment_page.select_month(credit_card_exp_date[0])
        self.payment_page.select_year(credit_card_exp_date[1])
        self.payment_page.input_cvv(credit_card_cvv)
        self.payment_page.input_cardholder_name(configfile.default_cardholder_name)
        self.payment_page.input_address1(configfile.default_address1)
        self.payment_page.input_address2(configfile.default_address2)
        self.payment_page.input_city(configfile.default_city)
        self.payment_page.input_postal_code(configfile.default_postcode)
        self.payment_page.select_billing_address_country(configfile.default_country)
        self.payment_page.accept_terms()
        self.payment_page.click_pay_now()
        self.payment_page.wait_for_payment_result()

    @fun_call_decorator
    def check_payment_result(self):
        try:
            logging.info('Checking if payment declined message appeared.')
            result = self.payment_page.check_prompt()
            assert result, 'Payment declined message not found.'
            logging.info('Payment declined message found')
        except:
            logging.exception()
        finally:
            self.driver.close()

if __name__ == '__main__':
    ver = PaymentVerifier()
    ver.fill_in_flight_details('DUB','SXF','15/05/2016','2','1')
    ver.provide_payment_details('5555555555555557','10/2018','123')
    ver.check_payment_result()