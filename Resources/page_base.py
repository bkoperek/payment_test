# -*- coding: utf-8 -*-
__author__= 'bartosz_koperek'

import logging
import exceptions
from config import configfile
from random import choice
from string import lowercase
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):
    def __init__(self,driver):
        logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s",level=logging.DEBUG)
        self.driver = driver

    def check_if_page_is_loaded(self,by,locator,timeout=configfile.timeout_check_if_page_is_loaded):
        logging.info('Checking if page is loaded properly.')
        try:
            self.find_element(by,locator)
            logging.info('Page {} loaded.'.format(self.driver.current_url))
        except TimeoutException:
            logging.exception('Timeout exception occured!')
            raise exceptions.PageNotLoadedError('Page not loaded properly!')

    def click_element(self,locator,by):
        element = self.find_element(by,locator)
        element.click()

    def click_and_wait(self,locator,by,timeout=configfile.timeout_wait_for_change):
        source = self.driver.page_source
        element = self.find_element(by,locator)
        element.click()
        def compare_source(driver):
            try:
                return source != driver.page_source
            except WebDriverException:
                pass
        WebDriverWait(self.driver, timeout).until(compare_source)

    def wait_for_change(self,timeout=configfile.timeout_wait_for_change):
        source = self.driver.page_source
        def compare_source(driver):
            try:
                return source != driver.page_source
            except WebDriverException:
                pass
        WebDriverWait(self.driver, timeout).until(compare_source)

    def fill_element_by_text(self,locator,by,text):
        element = self.find_element(by,locator)
        element.click()
        element.clear()
        element.send_keys(text)
        return element

    def fill_element_by_text_and_send_tab(self,locator,by,text):
        element = self.fill_element_by_text(locator,by,text)
        element.send_keys(Keys.TAB)

    def fill_elements_by_random_text(self,locator,by):
        elements = self.find_elements(by,locator)
        for element in elements:
            element.clear()
            element.send_keys(self.generate_string())

    def generate_string(self,input_length=configfile.random_string_length):
        random_input = "".join(choice(lowercase) for i in range(input_length))
        return random_input

    def find_element(self,by,locator,timeout=configfile.timeout_find_element):
        if by == 'id':
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID,locator)))
        elif by == 'xpath':
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH,locator)))
        elif by == 'name':
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.NAME,locator)))
        elif by == 'class':
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME,locator)))
        return element

    def find_elements(self,by,locator,timeout=configfile.timeout_find_element):
        if by == 'id':
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.ID,locator)))
        elif by == 'xpath':
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH,locator)))
        elif by == 'name':
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.NAME,locator)))
        elif by == 'class':
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME,locator)))
        return elements

    def select_element(self,by,value,element):
        select = Select(element)
        if by == 'id':
            select.select_by_index(value)
        elif by == 'text':
            select.select_by_visible_text(value)