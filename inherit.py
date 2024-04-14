import inspect
import logging

import pytest
from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("webbrowser")

class Baseclass:
    def VerifyText(self,text):
        mywait = WebDriverWait(self.driver, 20, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException])

        mywait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))
    def getLogger(self):
        loggingName=inspect.stack()[1][3]
        logger=logging.getLogger(loggingName)
        filehandler=logging.FileHandler("logs.log")
        formatter=logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)

        return logger