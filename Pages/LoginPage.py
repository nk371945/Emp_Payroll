import time

from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from selenium.webdriver.common.by import By
from utilities import PropertyFile, ExcelUtil


class LoginPage(BasePage):
    USERNAME = (By.XPATH, "//input[@placeholder='Email']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGINBTN = (By.XPATH, "//button[contains(@class,'btn btn-primary')]")
    ALERT = (By.XPATH, "//p[@class='alert alert-danger']")

    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self, username, password, sheet_name, rownum):
        self.clearAndType(self.USERNAME, username)
        self.clearAndType(self.PASSWORD, password)
        #ScreenShot.takeScreenshot(self.driver, 'credentials_filled')
        time.sleep(3)
        self.click(self.LOGINBTN)
        time.sleep(15)
        try:
            assert "Inbox - Odoo" == self.driver.title
            #ScreenShot.takeScreenshot(self.driver, 'successfully_logged_in')
            if rownum != 0:
                ExcelUtil.write_data(PropertyFile.getValues('test_report_file'),
                                     sheet_name, rownum, 6,
                                     "Redirected to HomePage")
                ExcelUtil.write_data(PropertyFile.getValues('test_report_file'),
                                     sheet_name, rownum, 7,
                                     'Pass')
            return HomePage(self.driver)
        except AssertionError:
            value = self.getText(self.ALERT)
            #ScreenShot.takeScreenshot(self.driver, value)
            if rownum != 0:
                ExcelUtil.write_data(PropertyFile.getValues('test_report_file'),
                                     sheet_name, rownum, 6,
                                     value)
                ExcelUtil.write_data(PropertyFile.getValues('test_report_file'),
                                     sheet_name, rownum, 7,
                                     'Pass')
            return None
