# -*- coding: utf-8 -*-
__author__= 'bartosz_koperek'

from page_base import BasePage
import logging

class Payment(BasePage):
    INPUTS_PASSENGERS_XPATH_LOCATOR = '//ng-form[@name="passengersForm"]/descendant::input'
    INPUTS_TITLES_XPATH_LOCATOR = '//ng-form[@name="passengersForm"]/descendant::select'
    INPUT_EMAIL_XPATH_LOCATOR = '//input[@placeholder="Enter email address"]'
    INPUT_PHONE_NUMBER_XPATH_LOCATOR = '//input[@name="phoneNumber"]'
    INPUT_CARD_NUMBER_XPATH_LOCATOR = '//input[@name="cardNumber"]'
    INPUT_SECURITY_CODE_XPATH_LOCATOR = '//input[@name="securityCode"]'
    INPUT_CARDHOLDER_NAME_XPATH_LOCATOR = '//input[@name="cardHolderName"]'
    INPUT_ADDRESS1_XPATH_LOCATOR = '//input[@name="billingAddressAddressLine1"]'
    INPUT_ADDRESS2_XPATH_LOCATOR = '//input[@name="billingAddressAddressLine2"]'
    INPUT_CITY_XPATH_LOCATOR = '//input[@name="billingAddressCity"]'
    INPUT_POSTCODE_XPATH_LOCATOR = '//input[@name="billingAddressPostcode"]'
    INPUT_ACCEPT_TERMS_XPATH_LOCATOR = '//input[@name="acceptPolicy"]'
    SELECT_PHONE_NUMBER_COUNTRY_XPATH_LOCATOR = '//select[@name="phoneNumberCountry"]'
    SELECT_CARD_TYPE_XPATH_LOCATOR = '//select[@name="cardType"]'
    SELECT_EXPIRY_MONTH_XPATH_LOCATOR = '//select[@name="expiryMonth"]'
    SELECT_EXPIRY_YEAR_XPATH_LOCATOR = '//select[@name="expiryYear"]'
    SELECT_BILLING_COUNTRY_XPATH_LOCATOR = '//select[@name="billingAddressCountry"]'
    BUTTON_PAYNOW_XPATH_LOCATOR = '//button[@translate="common.components.payment_forms.pay_now"]'
    PROMPT_PAYMENT_DECLINED_XPATH_LOCATOR = '//prompt[@ng-switch-when="PaymentDeclined"]'
    PASSENGERS_FORM_XPATH_LOCATOR = '//ng-form[@name="passengersForm"]'

    def __init__(self,driver):
        logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s",level=logging.DEBUG)
        logging.debug('New object of class {} constructed'.format(self.__class__.__name__))
        self.driver = driver

    def check_webpage(self):
        self.check_if_page_is_loaded('xpath',self.PASSENGERS_FORM_XPATH_LOCATOR)

    def generate_passengers(self):
        logging.info('Providing passengers details.')
        self.fill_elements_by_random_text(self.INPUTS_PASSENGERS_XPATH_LOCATOR,'xpath')

    def choose_titles(self,default_title):
        titles = self.find_elements('xpath',self.INPUTS_TITLES_XPATH_LOCATOR)
        for title in titles:
            self.select_element('text',default_title,title)

    def input_email(self,email):
        logging.info('Entering email.')
        self.fill_element_by_text(self.INPUT_EMAIL_XPATH_LOCATOR,'xpath',email)

    def select_country(self,default_country):
        logging.info('Selecting phone number country.')
        country = self.find_element('xpath',self.SELECT_PHONE_NUMBER_COUNTRY_XPATH_LOCATOR)
        self.select_element('text',default_country,country)

    def input_phone_number(self,number):
        logging.info('Entering phone number.')
        self.fill_element_by_text(self.INPUT_PHONE_NUMBER_XPATH_LOCATOR,'xpath',number)

    def input_card_number(self,card_number):
        logging.info('Entering card number.')
        card_number = card_number.replace(' ','')
        self.fill_element_by_text(self.INPUT_CARD_NUMBER_XPATH_LOCATOR,'xpath',card_number)

    def select_card_type(self,default_type):
        logging.info('Selecting card type.')
        card_type = self.find_element('xpath',self.SELECT_CARD_TYPE_XPATH_LOCATOR)
        self.select_element('text',default_type,card_type)

    def select_month(self,month_text):
        logging.info('Selecting credit card expiration date.')
        month = self.find_element('xpath',self.SELECT_EXPIRY_MONTH_XPATH_LOCATOR)
        self.select_element('text',month_text,month)

    def select_year(self,year_text):
        year = self.find_element('xpath',self.SELECT_EXPIRY_YEAR_XPATH_LOCATOR)
        self.select_element('text',year_text,year)

    def input_cvv(self,cvv_text):
        logging.info('Entering CVV.')
        self.fill_element_by_text(self.INPUT_SECURITY_CODE_XPATH_LOCATOR,'xpath',cvv_text)

    def input_cardholder_name(self,cardholder_name):
        logging.info('Entering cardholder name.')
        self.fill_element_by_text(self.INPUT_CARDHOLDER_NAME_XPATH_LOCATOR,'xpath',cardholder_name)

    def input_address1(self,address1_text):
        logging.info('Entering billing details part 1.')
        self.fill_element_by_text(self.INPUT_ADDRESS1_XPATH_LOCATOR,'xpath',address1_text)

    def input_address2(self,address2_text):
        logging.info('Entering billing details part 2.')
        self.fill_element_by_text(self.INPUT_ADDRESS2_XPATH_LOCATOR,'xpath',address2_text)

    def input_city(self,city_text):
        logging.info('Entering billing details - city.')
        self.fill_element_by_text(self.INPUT_CITY_XPATH_LOCATOR,'xpath',city_text)

    def input_postal_code(self,postcode_text):
        logging.info('Entering postcode.')
        self.fill_element_by_text(self.INPUT_POSTCODE_XPATH_LOCATOR,'xpath',postcode_text)

    def select_billing_address_country(self,country_text):
        logging.info('Selecting billing country.')
        country = self.find_element('xpath',self.SELECT_BILLING_COUNTRY_XPATH_LOCATOR)
        self.select_element('text',country_text,country)

    def accept_terms(self):
        logging.info('Accepting terms.')
        self.click_element(self.INPUT_ACCEPT_TERMS_XPATH_LOCATOR,'xpath')

    def click_pay_now(self):
        logging.info('Clicking pay now.')
        self.click_and_wait(self.BUTTON_PAYNOW_XPATH_LOCATOR,'xpath')

    def wait_for_payment_result(self):
        logging.info('Waiting for payment result.')
        self.wait_for_change()

    def check_prompt(self):
        prompt = self.driver.find_element_by_xpath(self.PROMPT_PAYMENT_DECLINED_XPATH_LOCATOR)
        if prompt:
            return True
        else:
            return False

