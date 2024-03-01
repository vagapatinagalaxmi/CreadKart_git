from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class check_list:
    Text_username_Xpath = "//input[@name='email']"
    Text_password_Xpath = "//input[@id='password']"
    Click_save_Xpath = "//button[@type='submit']"

    Click_image_Xpath = "//img[@src='https://automation.credence.in/img/macbook-pro.jpg']"
    Click_Add_cart_Xpath = "//input[@value='Add to Cart']"
    Click_proceed_Xpath = "//a[@class='btn btn-success btn-lg']"
    Text_Firstname_Xpath = "//input[@id='first_name']"
    Text_Lastname_Xpath = "//input[@id='last_name']"
    Text_Phone_no_Xpath = "//input[@id='phone']"
    Text_Address_Xpath = "//textarea[@id='address']"
    Text_Zip_Xpath = "//input[@id='zip']"
    Text_State_Xpath = "//select[@id='state']"
    Text_Owner_Xpath = "//input[@id='owner']"
    Text_CVV_Xpath = "//input[@id='cvv']"
    Text_Year_Xpath = "//select[@id='exp_year']"
    Text_Month_Xpath = "//select[@id='exp_month']"
    Text_Card_no_Xpath = "//input[@id='cardNumber']"
    Click_Confirm_button_Xpath = "//button[@id='confirm-purchase']"
    Text_Verify_Xpath = "/html/body/div/div[1]/p[1]"

    def __init__(self, driver):
        self.driver = driver

    def username(self, name):
        self.driver.find_element(By.XPATH, self.Text_username_Xpath).send_keys(name)

    def password(self, password):
        self.driver.find_element(By.XPATH, self.Text_password_Xpath).send_keys(password)

    def Click_save(self):
        self.driver.find_element(By.XPATH, self.Click_save_Xpath).click()

    def Click_image(self):
        self.driver.find_element(By.XPATH, self.Click_image_Xpath).click()

    def Add_cart(self):
        self.driver.find_element(By.XPATH, self.Click_Add_cart_Xpath).click()

    def proceed(self):
        self.driver.find_element(By.XPATH, self.Click_proceed_Xpath).click()

    def Firstname(self, name):
        self.driver.find_element(By.XPATH, self.Text_Firstname_Xpath).send_keys(name)

    def Lastname(self, l_name):
        self.driver.find_element(By.XPATH, self.Text_Lastname_Xpath).send_keys(l_name)

    def Phone_number(self, number):
        self.driver.find_element(By.XPATH, self.Text_Phone_no_Xpath).send_keys(number)

    def Address(self, add):
        self.driver.find_element(By.XPATH, self.Text_Address_Xpath).send_keys(add)

    def Zip(self, z):
        self.driver.find_element(By.XPATH, self.Text_Zip_Xpath).send_keys(z)

    def State(self):
        Select(self.driver.find_element(By.XPATH, self.Text_State_Xpath)).select_by_index(2)

    def Owner(self, name):
        self.driver.find_element(By.XPATH, self.Text_Owner_Xpath).send_keys(name)

    def Cvv(self, no):
        self.driver.find_element(By.XPATH, self.Text_CVV_Xpath).send_keys(no)

    def year(self):
        Select(self.driver.find_element(By.XPATH, self.Text_Year_Xpath)).select_by_index(2)

    def month(self):
        Select(self.driver.find_element(By.XPATH, self.Text_Month_Xpath)).select_by_index(2)

    def Card_no(self, no):
        self.driver.find_element(By.XPATH, self.Text_Card_no_Xpath).send_keys(no)

    def Card_no1(self, no):
        self.driver.find_element(By.XPATH, self.Text_Card_no_Xpath).send_keys(no)

    def Card_no2(self, no):
        self.driver.find_element(By.XPATH, self.Text_Card_no_Xpath).send_keys(no)

    def Card_no3(self, no):
        self.driver.find_element(By.XPATH, self.Text_Card_no_Xpath).send_keys(no)

    def Click_confirm(self):
        self.driver.find_element(By.XPATH, self.Click_Confirm_button_Xpath).click()

    def verify(self):
        try:
            self.driver.find_element(By.XPATH, self.Text_Verify_Xpath)
            return "pass"
        except:
            return "Fail"
