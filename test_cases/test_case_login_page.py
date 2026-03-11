import pytest
from selenium import webdriver
from base_pages.login_page import LoginPage
from utilities.read_popertice import read_popertice
from selenium.webdriver.common.by import By



class Test_login_page():
    def test_tittle_varification(self,setup):
        self.driver =setup
        self.driver.get(read_popertice.get_url())
        act_title = self.driver.title
        exp_title = "Automation Exercise"
        assert act_title == exp_title,"The title is not matched, you enterd in the wrong website"
        

    def test_valid_login(self,setup):
        self.driver = setup
        self.driver.get(read_popertice.get_url())
        self.login = LoginPage(self.driver)
        self.login.go_to_login_page()
        self.login.fill_email_input(read_popertice.get_email_address())
        self.login.fill_password_input(read_popertice.get_password())
        self.login.click_login_btn()
        #chacking the title for the test cases are passed

        login_user = self.driver.find_element(By.XPATH,"//a[contains(text(),' Logged in as ')]")
        assert login_user.is_displayed(), "Login fail chack the massage. "
        
       
