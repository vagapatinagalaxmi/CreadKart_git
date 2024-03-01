import time

import allure
import pytest
from allure_commons.types import AttachmentType

from PageObject.chechklistpage import check_list
from Utilities.logger import logGenerater
from Utilities.readconfig import Readconfig





class Test_list:
    Useremail = Readconfig.getUsername()
    Password = Readconfig.getPassword()
    log = logGenerater.loggen()

    @pytest.mark.usefixtures("setup")
    def test_checklist(self,setup):
        self.log.info("Testcase test_Checklist started")
        self.log.info("Browser navigated to https://automation.credence.in/logindKart.com")
        self.driver=setup
        self.cl=check_list(self.driver)
        self.driver.get("https://automation.credence.in/login")
        self.log.info("Enter useremail")
        self.cl.username(self.Useremail)
        self.log.info("Enter Password")
        self.cl.password(self.Password)
        self.log.info("Click Save Button")
        self.cl.Click_save()
        self.log.info("Click  MocBook image")
        self.cl.Click_image()
        self.log.info("Click Add to cart")
        self.cl.Add_cart()
        self.log.info("Click Proceed")
        self.cl.proceed()
        self.log.info("Enter firstname")
        self.cl.Firstname("shivansh")
        self.log.info("Enter Lastname")
        self.cl.Lastname("nadukula")
        self.log.info("Enter Phone.no")
        self.cl.Phone_number("9091929355")
        self.log.info("Enter Address")
        self.cl.Address("kul echo delight")
        self.log.info("Enter Zip number")
        self.cl.Zip("456789")
        self.log.info("Enter state")
        self.cl.State()
        self.log.info("Enter Owner name")
        self.cl.Owner("shivansh")
        self.log.info("Enter Cvv number")
        self.cl.Cvv("345")
        self.log.info("Enter year")
        self.cl.year()
        self.log.info("Enter month")
        self.cl.month()
        self.log.info("Enter Card Number")
        self.cl.Card_no("5281")
        self.cl.Card_no1("0370")
        self.cl.Card_no2("4891")
        self.cl.Card_no3("6168")
        self.log.info("Click comform Button")
        self.cl.Click_confirm()
        time.sleep(5)
        if self.cl.verify()=="pass":
            self.log.info("Tst Case test_checklist passed")
            self.log.info("Take the Screenshot")
            self.driver.save_screenshot("C:\\python fixture\\credKart\\Screenshots\\test_checklist_pass.png")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_checklist_pass.png",
                          attachment_type=AttachmentType.PNG)
            assert True
        else:
            self.log.info("Teat case test_checklist failed")
            self.driver.save_screenshot("C:\\python fixture\\credKart\\Screenshots\\test_checklist_fail.png")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_checklist_fail.png",
                          attachment_type=AttachmentType.PNG)
            self.log.info("Take Screenshot")
            assert False
        self.log.info("Test case test_checklist completed")