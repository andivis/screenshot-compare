import sys
import os
import logging
import datetime
import traceback
import smtplib

import program.library.helpers as helpers

from program.library.helpers import get
from program.library.selenium import Selenium

class Main:
    def run(self):
        logging.info('Starting')

        file = helpers.getFile(self.options['inputFile'])

        self.inputRows = file.splitlines()

        for i, self.inputRow in enumerate(self.inputRows):
            try:
                logging.info(f'Line {i + 1} of {len(self.inputRows)}: {self.inputRow}')

                self.browser.getScreenshot(self.inputRow, self.getOutputFileName(self.inputRow), self.options['secondsBeforeScreenshot'], self.options['browser'])
            except Exception as e:
                helpers.handleException(e)
        
        self.cleanUp()

    def removeMiddle(self, string, maximumLength):
        result = string

        if len(result) > maximumLength:
            half = maximumLength//2

            result = result[0:half] + '...' + result[-half:]

        return result

    def getOutputFileName(self, inputRow):
        result = self.options['outputDirectory']

        date = datetime.datetime.now().strftime('%Y-%m-%d.%H.%M.%S')
        
        inputRow = helpers.findBetween(inputRow, '://www.', '')
        inputRow = helpers.findBetween(inputRow, '://', '')
        inputRow = helpers.lettersNumbersAndSpecifiedOnly(inputRow, ['.'])
        
        name = self.removeMiddle(inputRow, 75) + '-' + date + '.png'

        return os.path.join(result, name)

    def cleanUp(self):
        self.browser.shutdown()
        logging.info('Done')

    def __init__(self, siteToRun='', modeToRun=''):
        helpers.setUpLogging('user-data/logs')

        # set default options
        self.options = {
            'inputFile': 'user-data/input/input.txt',
            'outputDirectory': 'user-data/output',
            'browser': 'chrome',
            'emailAddress': '',
            'secondsBeforeScreenshot': '1'
        }

        optionsFileName = helpers.getParameter('--optionsFile', False, 'user-data/options.ini')
        
        # read the options file
        helpers.setOptions(optionsFileName, self.options)

        helpers.makeDirectory(self.options['outputDirectory'])

        self.browser = Selenium()

if __name__ == '__main__':
    main = Main()
    main.run()