import sys
import os
import time
import logging

# pip packages
from selenium import webdriver

from . import helpers

from .helpers import get

class Selenium:
    def getScreenshot(self, url, fileName, secondsBeforeScreenshot, browser='chrome'):
        self.initialize(browser)

        self.driver.get(url)

        if secondsBeforeScreenshot:
            helpers.wait(secondsBeforeScreenshot)

        self.driver.save_screenshot(fileName)

    def shutdown(self):
        if self.driver:
            self.driver.quit()

    def initialize(self, browser):
        if self.initialized:
            return

        self.initialized = True

        if browser == 'chrome':
            chromedriver = "chromedriver.exe"
            self.driver = webdriver.Chrome(chromedriver)
        else:
            self.driver = webdriver.Firefox()
    
    def __init__(self):
        self.initialized = False
        self.driver = None
