import sys
import os
import time
import logging

# pip packages
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from . import helpers

from .helpers import get

class Selenium:
    def getScreenshot(self, url, fileName, secondsBeforeScreenshot, browser='chrome'):
        self.initialize(browser)

        self.driver.get(url)

        if secondsBeforeScreenshot:
            helpers.wait(secondsBeforeScreenshot)

        element = self.driver.find_element_by_tag_name('body')
        element_png = element.screenshot_as_png
        
        with open(fileName, "wb") as file:
            file.write(element_png)

    def shutdown(self):
        if self.driver:
            self.driver.quit()

    def initialize(self, browser):
        if self.initialized:
            return

        self.initialized = True

        if browser == 'chrome':
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1280x720")
            
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        else:
            options = webdriver.firefox.options.Options()
            options.headless = True

            self.driver = webdriver.Firefox(options=options)
    
    def __init__(self):
        self.initialized = False
        self.driver = None
