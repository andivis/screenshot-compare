import sys
import os
import logging
import datetime
import traceback
import smtplib

import program.library.helpers as helpers

from program.library.helpers import get

class Main:
    def run(self):
        logging.info('Starting')

        
        
        self.cleanUp()

    def cleanUp(self):
        logging.info('Done')

    def setOptions(self):
        # set default options
        self.options = {
            'inputFile': 'user-data/input/input.txt',
            'emailAddress': ''
        }

        optionsFileName = helpers.getParameter('--optionsFile', False, 'user-data/options.ini')
        
        # read the options file
        helpers.setOptions(optionsFileName, self.options)

    def __init__(self, siteToRun='', modeToRun=''):
        helpers.setUpLogging('user-data/logs')

if __name__ == '__main__':
    main = Main()
    main.run()