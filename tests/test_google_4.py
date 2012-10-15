'''
Created on 12.10.2012

@author: cbalea
'''
from selenium import webdriver
import time
import unittest

class TestGoogle4(unittest.TestCase):
    
    
    def initializeFirefoxDriver(self):
        driver = webdriver.Firefox()
        return driver
    
    def common(self):
        self.driver = self.initializeFirefoxDriver()
        self.driver.get("http://www.google.com")
        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys("Cheese!")
        inputElement.submit()
        time.sleep(1)


    def test_4_1(self):
        self.common()
        print "Test 4_1: " + self.driver.title
    
    def test_4_2(self):
        self.common()
        print "Test 4_2: " + self.driver.title
    
#    def test_4_3(self):
#        self.common()
#        print "Test 4_3: " + self.driver.title
#    
#    def test_4_4(self):
#        self.common()
#        print "Test 4_4: " + self.driver.title
#    
#    def test_4_5(self):
#        self.common()
#        print "Test 4_5: " + self.driver.title

    def tearDown(self):
        self.driver.quit()
