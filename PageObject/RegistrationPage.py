# 26/1/2024
from selenium.webdriver.common.by import By


class UserRegistration:

    Click_Registration_Xpath = "//a[text()='Register']"
    Text_Username_Name = "name"
    Text_Email_Name = "email"
    Text_Password_XPATH = "//*[@id='password']"
    Text_ConformPassword_XPATH= "//*[@id='password-confirm']"
    Click_Button_XPATH = "/html/body/div/div/div/div/div[2]/form/div[5]/div/button"
    Validate_Status_XPATH = "//h2[normalize-space()='CredKart']"

    def __init__(self, driver):

        self.driver = driver

    def Click(self):
        self.driver.find_element(By.XPATH, self.Click_Registration_Xpath).click()

    def Enter_Username(self, username):
        self.driver.find_element(By.NAME, self.Text_Username_Name).send_keys(username)

    def Enter_Email(self, email):
        self.driver.find_element(By.NAME, self.Text_Email_Name).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(By.XPATH, self.Text_Password_XPATH).send_keys(password)

    def Enter_ConformPassword(self, conformPassword):
        self.driver.find_element(By.XPATH, self.Text_ConformPassword_XPATH).send_keys(conformPassword)

    def Click_button(self):
        self.driver.find_element(By.XPATH, self.Click_Button_XPATH).click()



    def Validation(self):
        try:
            self.driver.find_element(By.XPATH, self.Validate_Status_XPATH)
            print("TEST CASE PASSEd")
            return "TEST CASE PASSED"
        except:
            print("TEST CASE FAIL")
            return "TEST CASE FAIL"