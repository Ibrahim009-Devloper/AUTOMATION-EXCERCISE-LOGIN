from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():
    get_login_btn = (By.XPATH,"//a[contains(text(),' Login')]")
    get_email_el = (By.NAME,"email")
    get_password_el = (By.NAME,"password")
    click_login_btn_el = (By.XPATH,"//button[contains(text(),'Login')]")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def go_to_login_page(self):
        self.wait.until(EC.element_to_be_clickable(self.get_login_btn)).click()

    def fill_email_input(self,email):
        el = self.wait.until(EC.visibility_of_element_located(self.get_email_el))
        el.clear()
        el.send_keys(email)

    def fill_password_input(self,password):
        pwd = self.wait.until(EC.visibility_of_element_located(self.get_password_el))
        pwd.clear()
        pwd.send_keys(password)

    def click_login_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.click_login_btn_el)).click()

