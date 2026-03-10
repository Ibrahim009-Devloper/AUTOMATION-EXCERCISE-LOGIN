import pytest
from selenium import webdriver
from base_pages.login_page import LoginPage
from utilities.read_popertice import read_popertice



class Test_login_page():
    def test_tittle_varification(self):
        self.driver =webdriver.Chrome()
        self.driver.get(read_popertice.get_url())
        act_title = self.driver.title
        exp_title = "Automation Exercise"
        assert act_title == exp_title,"The title is not matched, you enterd in the wrong website"
        self.driver.quit()

    def test_valid_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(read_popertice.get_url())
        self.login = LoginPage(self.driver)
        self.login.go_to_login_page()
        self.login.fill_email_input(read_popertice.get_email_address())
        self.login.fill_password_input(read_popertice.get_password())
        self.login.click_login_btn()
        #chacking the title for the test cases are passed
        act_title = self.driver.title
        exp_title = "Automation Exercise"
        assert act_title == exp_title,"The title is not matching. chack the code"
        self.driver.quit()
