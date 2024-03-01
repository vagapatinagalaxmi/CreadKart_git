# 26/1/2024
import allure
import pytest
import time
import random
import string

from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

# from PageObject import RegistrationPage
from PageObject.RegistrationPage import UserRegistration
from selenium import webdriver
from Utilities.logger import logGenerater





@pytest.mark.usefixtures("setup")
class Test_UserRegistration:
    log = logGenerater.loggen()

    def test_UserReg(self, setup):
        self.log .info("Testcase started Test_UserRegistration")
        # self.log.info("this is info")
        # self.log.warning("this is warning")
        # self.log.error("this is error")
        # self.log.critical("this is critical")
        self.log.info("browser opened")
        self.driver = setup
        self.ur = UserRegistration(self.driver)
        self.driver.get("https://automation.credence.in")

        self.ur.Click()

        self.log.info("Entering uasername")
        username=self.ur.Enter_Username("credencetesting")
        self.log.info("Enter_Username--->"+ str(username))
        self.log.info("Generating Random Email")
        email = Generate_Email
        self.ur.Enter_Email(Generate_Email())
        self.log.info( "entering random email")
        self.log.info("generateemail-->"+str(email))
        print("generateemail-->" + str(email))
        self.log.info("entering password")
        self.ur.Enter_Password("test@1234")
        self.log.info("entering conformpassword")
        self.ur.Enter_ConformPassword("test@1234")

        self.log.info("click_Register_Button")
        self.ur.Click_button()

        if self.ur.Validation() == "TEST CASE PASSED":
            self.log.info("Test case test_UserRegistration passed")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_registration_pass.png",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("C:\\python fixture\\credKart\\Screenshots\\test_UserReg_pass.png")
            assert True

        else:
            self.log.info("Test case test_UserRegistration Failed")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_registration_fail",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("C:\\python fixture\\credKart\\Screenshots\\test_UserReg_fail.png")
            assert False
        self.log.info("Test case test_UserRegistration completed")


def Generate_Email():

    username = ''.join(random.choices(string.ascii_lowercase, k=4))  # rondam 4 char lower case e.g gfhd
    domain = random.choice(['gmail.com', 'yahoo.com', 'outlook.com'])  #
    return f"{username}@{domain}"  # random 4 char + domain
