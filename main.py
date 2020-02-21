import sys
import os
import logging
import datetime
import traceback
import random
import string

from pathlib import Path

if not os.path.exists('program/library/selenium.py'):
    home = str(Path.home())
    os.chdir(home + '/screenshot-compare')
    sys.path.append(home + '/screenshot-compare')

import program.library.helpers as helpers

from program.library.helpers import get
from program.library.selenium import Selenium
from program.library.images import Images
from program.library.email import Email

class Main:
    def run(self):
        logging.info('Starting')

        file = helpers.getFile(self.options['inputFile'])

        inputRows = []

        if self.options['url']:
            inputRows = [self.options['url']]
        else:
            inputRows = file.splitlines()

        for i, inputRow in enumerate(inputRows):
            try:
                logging.info(f'Url {i + 1} of {len(inputRows)}: {inputRow}')

                self.currentFileName = self.getOutputFileName(inputRow)
                self.browser.getScreenshot(inputRow, self.currentFileName, self.options['secondsBeforeScreenshot'], self.options['browser'])

                information = self.compareWithPrevious(self.currentFileName)

                if information:
                    self.sendEmail(inputRow, information)
            except Exception as e:
                helpers.handleException(e)
        
        self.cleanUp()

    def compareWithPrevious(self, newFileName):
        result = {}

        directory = os.path.dirname(newFileName)

        files = helpers.listFiles(directory)
        files.sort()
        files.reverse()
        
        oldFileName = None
        
        # get second oldest file
        for file in files:
            if file != newFileName:
                oldFileName = file
                break

        if not oldFileName:
            logging.info('Nothing to compare with yet')
            return result

        percentage = self.percentageDifference(oldFileName, newFileName)

        if percentage > self.options['allowedDifference']:
            logging.info(f'More than {self.options["allowedDifference"]}% different. Sending email.')
            
            result = {
                'oldFileName': oldFileName,
                'newFileName': newFileName,
                'percentage': percentage
            }
        else:
            logging.info(f'Less than or equal to {self.options["allowedDifference"]}% difference. Not sending email.')

        return result
        
    def sendEmail(self, url, information):
        percentage = get(information, 'percentage')
        percentage = helpers.fixedDecimals(percentage, 3)

        message = f'The screenshot for {url} is {percentage}% different than the previous screenshot.'
            
        self.email.sendEmail(self.options['emailAddress'], 'Screenshot changed', message)

    def percentageDifference(self, file1, file2):
        logging.info(f'Comparing {file1} and {file2}')

        images = Images()
        try:
            result = images.differencePercentage(file1, file2)
        except Exception as e:
            logging.error(e)
            result = 100

        logging.info(f'Difference {result}%')
        
        return result

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
        
        subdirectory = self.getId(inputRow) + '-' + self.removeMiddle(inputRow, 75)

        name = date + '.png'

        result = os.path.join(result, subdirectory, name)

        helpers.makeDirectory(os.path.dirname(result))

        return result

    def getId(self, url):
        result = ''

        file = helpers.getFile('user-data/logs/cache.txt')

        for line in file.splitlines():
            lineUrl = helpers.findBetween(line, ' ', '')

            if lineUrl == url:
                result = helpers.findBetween(line, '', ' ')
                break

        if not result:
            result = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))

            helpers.appendToFile(f'{result} {url}', 'user-data/logs/cache.txt')

        return result

    def cleanUp(self):
        self.browser.shutdown()
        logging.info('Done')

    def setParameters(self, parameters, options):
        result = options
        
        for parameter, possibleNames in parameters.items():
            for possibleName in possibleNames:
                value = helpers.getParameter(possibleName, False)

                if value:
                    if isinstance(get(options, parameter), int):
                        result[parameter] = int(value)
                    else:
                        result[parameter] = value

        return result

    def __init__(self, siteToRun='', modeToRun=''):
        helpers.setUpLogging('user-data/logs')

        # set default options
        self.options = {
            'inputFile': 'user-data/input/input.txt',
            'outputDirectory': 'user-data/output',
            'browser': 'firefox',
            'emailAddress': '',
            'url': '',
            'smtpHost': '',
            'smtpPort': '',
            'smtpUsername': '',
            'smtpPassword': '',
            'secondsBeforeScreenshot': '1',
            'allowedDifference': 5
        }

        optionsFileName = helpers.getParameter('--optionsFile', False, 'user-data/options.ini')
        
        # read the options file
        helpers.setOptions(optionsFileName, self.options)

        parameters = {
            'url': ['-u', '--url'],
            'emailAddress': ['-e', '--email'],
            'allowedDifference': ['-m', '--max-difference']
        }

        self.options = self.setParameters(parameters, self.options)

        helpers.makeDirectory(self.options['outputDirectory'])

        self.browser = Selenium()
        self.email = Email(self.options)

if __name__ == '__main__':
    main = Main()
    main.run()