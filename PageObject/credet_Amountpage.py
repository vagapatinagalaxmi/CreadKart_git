# 31/1/2024
import time
from _ast import Global
from typing import Any

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait






class CreadAmountClass:
    Click_image1_Xpath = "//img[@src='https://automation.credence.in/img/macbook-pro.jpg']"

    Click_Addtocart1_Xpath = "//input[@value='Add to Cart']"
    Click_Countinue1_Xpath = "//a[@class='btn btn-primary btn-lg']"
    Click_image2_xpath = "//img[@src='https://automation.credence.in/img/headphones.jpg']"
    Click_AddtoCart2_Xpath = "//input[@value='Add to Cart']"
    Click_Countinue2_Xpath = "//a[@class='btn btn-primary btn-lg']"
    Click_image3_Xpath = "//img[@src='https://automation.credence.in/img/ipad-retina.jpg']"
    Click_Addtocart3_Xpath = "//input[@value='Add to Cart']"
    Click_Dropdown1_Xpath = "//tbody/tr[1]/td[3]/select[1]"
    Click_Dropdown2_Xpath = "//tbody/tr[2]/td[3]/select[1]"
    Click_Dropdown3_Xpath = "//tbody/tr[3]/td[3]/select[1]"
    var1_Xpath = "/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]"
    var2_Xpath = "/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[2]/td[4]"
    var3_Xpath = "/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[3]/td[4]"
    var4_Xpath = "/html/body/div/table/tbody/tr[6]/td[4]"
    Click_Continue3_Xpath = "//a[@class='btn btn-primary btn-lg']"
    Validation_Status_XPATH = "//h2[contains(text(),'CredKart')]"

    def __init__(self, driver):

        self.driver = driver


    def Click_image1(self):
        self.driver.find_element(By.XPATH, self.Click_image1_Xpath).click()

    def AddtoCart1(self):
        self.driver.find_element(By.XPATH, self.Click_Addtocart1_Xpath).click()

    def Countinueshop1(self):
        self.driver.find_element(By.XPATH, self.Click_Countinue1_Xpath).click()

    def Click_image2(self):
        self.driver.find_element(By.XPATH, self.Click_image2_xpath).click()

    def Addtocart2(self):
        self.driver.find_element(By.XPATH, self.Click_AddtoCart2_Xpath).click()

    def ContinueShop2(self):
        self.driver.find_element(By.XPATH, self.Click_Countinue2_Xpath).click()

    def Click_image3(self):
        self.driver.find_element(By.XPATH, self.Click_image3_Xpath).click()

    def Addtocart3(self):
        self.driver.find_element(By.XPATH, self.Click_Addtocart3_Xpath).click()

    def Dropdown1(self, num1):

        try:
          Select(self.driver.find_element(By.XPATH, self.Click_Dropdown1_Xpath)).select_by_index(num1)
          WebDriverWait(self.driver,5).until(expected_conditions.element_located_to_be_selected((By.XPATH,self.Click_Dropdown1_Xpath)))

        except:
            pass


    def Dropdown2(self, num2):
        try:
         Select(self.driver.find_element(By.XPATH, self.Click_Dropdown2_Xpath)).select_by_index(num2)
         WebDriverWait(self.driver,7).until(expected_conditions.element_located_to_be_selected((By.XPATH,self.Click_Dropdown2_Xpath)))

        except:
            pass

    def Dropdown3(self, num3):
        try:
         Select(self.driver.find_element(By.XPATH, self.Click_Dropdown3_Xpath)).select_by_index(num3)
         WebDriverWait(self.driver,9).until(expected_conditions.element_located_to_be_selected((By.XPATH,self.Click_Dropdown3_Xpath)))

        except:
           pass
    def var11(self):

        self.var1 = self.driver.find_element(By.XPATH, self.var1_Xpath).text
        print(self.var1[1:])
        product1 = float(self.var1[1:])
        print(product1)
        print(type(product1))
        self.var2 = self.driver.find_element(By.XPATH, self.var2_Xpath).text
        print(self.var2[1:])
        product2 = float(self.var2[1:])
        print(product2)
        print(type(product2))
        self.var3 = self.driver.find_element(By.XPATH, self.var3_Xpath).text
        print(self.var3[1:])
        product3 = float(self.var3[1:])
        print(product3)
        print(type(product3))
        expected_subtotal = product1 + product2 + product3
        expected_subtotal1 = round(expected_subtotal, 2)
        expected_subtotal_tax = float(expected_subtotal * 0.13)
        print("expected_subtotal_tax;" + str(expected_subtotal_tax))
        subtotal = round(expected_subtotal_tax, 2)
        print("subtotal:" + str(subtotal))
        expectedtotal = round(expected_subtotal1 + subtotal, 2)
        print("expectedtotal:" + str(expectedtotal))
        self.var4 = self.driver.find_element(By.XPATH, self.var4_Xpath).text
        print(self.var4[1:])
        actualtotal1 = self.var4[1:].replace(',', "")
        actualtotal3 = float(actualtotal1)
        print(actualtotal3)
        print(type(actualtotal3))
        print("actualtotal3: " + str(actualtotal3))

        if expectedtotal == actualtotal3:
            print("test case pass")

        else:
            print("test case fail")

    def Continue_shop3(self):
        self.driver.find_element(By.XPATH, self.Click_Continue3_Xpath).click()

    def Validation(self):
        try:
            self.driver.find_element(By.XPATH, self.Validation_Status_XPATH)

            return "TEST CASE PASSED"
        except:

            return "TEST CASE FAIL"
