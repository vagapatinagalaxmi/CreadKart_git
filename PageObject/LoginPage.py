# 26/1/2024

from selenium.webdriver.common.by import By


class LoginPageClass:
    Text_Username_XPATH = "//input[@id='email']"
    Text_Password_XPATH = "//input[@id='password']"
    Text_Login_Button_XPATH = "/html/body/div/div/div/div/div[2]/form/div[4]/div/button"
    Validation_Status_XPATH = "//h2[contains(text(),'CredKart')]"

    def __init__(self, driver):

        self.driver = driver

    def Enter_Username(self, username):
        self.driver.find_element(By.XPATH, self.Text_Username_XPATH).send_keys(username)

    def Enter_Password(self, password):

        self.driver.find_element(By.XPATH, self.Text_Password_XPATH).send_keys(password)

    def Login_Button(self):

        self.driver.find_element(By.XPATH, self.Text_Login_Button_XPATH).click()

    def Validation(self):
        try:
            self.driver.find_element(By.XPATH, self.Validation_Status_XPATH)

            return "TEST CASE PASSED"
        except:

            return "TEST CASE FAIL"
