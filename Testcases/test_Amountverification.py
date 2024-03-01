import time

import allure
from allure_commons.types import AttachmentType

from PageObject.credet_Amountpage import CreadAmountClass
from Utilities.logger import logGenerater
from Utilities.readconfig import Readconfig
import pytest


@pytest.mark.usefixtures("setup")
class Test_Amount:
    log = logGenerater.loggen()

    def test_Amount_verify(self, setup):
        self.log.info("Test case test_Amount_verify started ")
        self.driver = setup
        self.cav = CreadAmountClass(self.driver)
        self.log.info("browser navigated to https://automation.credence.in")
        self.driver.get("https://automation.credence.in")

        self.log.info("Click image MocBook")
        self.cav.Click_image1()
        self.log.info("Click AddCart")
        self.cav.AddtoCart1()
        self.log.info("Click Continue  shopping")
        self.cav.Countinueshop1()
        self.log.info("Click image headphone")
        self.cav.Click_image2()
        self.log.info("Click AddCart")
        self.cav.Addtocart2()
        self.log.info("Click continue shopping")
        self.cav.ContinueShop2()
        self.log.info("Click image ipad")
        self.cav.Click_image3()
        self.log.info("Click AddCart")
        self.cav.Addtocart3()
        self.log.info("Click Dropdown box")
        self.cav.Dropdown1(4)
        self.log.info("Click DropDown box")
        self.cav.Dropdown2(3)
        self.log.info("Click Dropdown box")
        self.cav.Dropdown3(2)
        self.log.info("calculate the values")
        self.cav.var11()
        self.log.info("Click continue shopping")
        self.cav.Continue_shop3()

        if self.cav.Validation() == "TEST CASE PASSED":
            self.log.info("Test case test_Amount verification passed")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Amount_verify_pass.png",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshots\\test_Amount_verify__pass.png")

            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Amount_verify_fail.png",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("C:\\python fixture\\credKart\\Screenshots\\test_Amount_verify_fail.png")
            self.log.info("Test case test_Amount_verify Fail")
            assert False
        self.log.info("Testcase test_Amount_verify completed")
