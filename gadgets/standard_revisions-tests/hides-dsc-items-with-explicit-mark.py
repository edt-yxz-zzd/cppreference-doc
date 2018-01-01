# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class HidesDscItemsWithExplicitMark(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://en.cppreference.com/"
        self.verificationErrors = []
    
    def test_hides_dsc_items_with_explicit_mark(self):
        driver = self.driver
        driver.get(self.base_url + "/w/test-gadget-stdrev/hides-dsc-items-with-explicit-mark")
        try: self.assertRegexpMatches(driver.find_element_by_xpath("//body").text, r"^[\s\S]*std::not_visible_in_cxx98[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_xpath("//body").text, r"^[\s\S]*std::not_visible_in_cxx11[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_css_selector("select")).select_by_visible_text("C++98/03")
        try: self.assertNotRegexpMatches(driver.find_element_by_xpath("//body").text, r"^[\s\S]*std::not_visible_in_cxx98[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_xpath("//body").text, r"^[\s\S]*std::not_visible_in_cxx11[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_css_selector("select")).select_by_visible_text("C++11")
        try: self.assertRegexpMatches(driver.find_element_by_xpath("//body").text, r"^[\s\S]*std::not_visible_in_cxx98[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotRegexpMatches(driver.find_element_by_xpath("//body").text, r"^[\s\S]*std::not_visible_in_cxx11[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()