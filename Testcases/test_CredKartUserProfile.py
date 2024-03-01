# 26/1/2024
import allure
import pytest
from allure_commons.types import AttachmentType

from PageObject import LoginPage
from PageObject.LoginPage import LoginPageClass
import string
from selenium import webdriver
from Utilities.readconfig import Readconfig
from Utilities.logger import logGenerater


@pytest.mark.usefixtures("setup")
class Test_UserLogin:
    Useremail = Readconfig.getUsername()
    Password = Readconfig.getPassword()
    log = logGenerater.loggen()

    def test_UserLogin1(self, setup):
        self.log.info("Testcase test_CreadKartUserProfile started")
        self.log.info("Browser navigated to https://automation.credence.in/login")
        self.driver = setup
        self.lp = LoginPageClass(self.driver)
        self.driver.get("https://automation.credence.in/login")

        # self.log.info("this is info")
        # self.log.warning("this is warning")
        # self.log.error("this error")
        # self.log.critical("this is critical")

        self.lp.Enter_Username(self.Useremail)
        self.log.info("Enteru_username-->" + self.Useremail)
        # print("Useremail-->"+str(self.Useremail))
        self.lp.Enter_Password(self.Password)
        self.log.info("Enter_Password-->" + self.Password)
        # print("Password--->"+str(self.Password))
        self.lp.Login_Button()

        if self.lp.Validation() == "TEST CASE PASSED":
            self.log.info("Test case test-CredKartUserProfile passed")
            allure.attach(self.driver.get_screenshot_as_png(), name="Cred_kart_pass.png",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshots\\test_UserLogin1_pass.png")

            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Cred_Kart_fail.png",
                          attachment_typr=AttachmentType.PNG)
            self.driver.save_screenshot("C:\\python fixture\\credKart\\Screenshots\\test_UserLogin1_fail.png")
            self.log.info("Test case test-CredKartUserProfile Fail")
            assert False
        self.log.info("Testcase test_CredKartUserprofile completed")
