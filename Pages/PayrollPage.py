import time

from Pages import EmployeesPage
from Pages.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from utilities import ScreenShot, ExcelUtil, PropertyFile


class PayrollPage(BasePage):
    create = (By.XPATH, "//button[text()[normalize-space()='Create']]")
    search_more = (By.LINK_TEXT, "Search More...")
    employee_dropdown = (By.XPATH, "(//label[text()='Employee']/following::input)[1]")
    all_emp = '//td[@class="o_data_cell"][1]'
    from_date = (By.XPATH, "(//input[@name='date_from'])[1]")
    to_date = (By.XPATH, "(//input[@name='date_to'])[1]")
    structure_dropdown = (By.XPATH, "(//label[text()='Structure']/following::input)[1]")
    all_structure = '//li[@class="ui-menu-item"]'
    pay_slip_name = (By.NAME, "name")
    compute_sheet_btn = (By.XPATH, "//span[text()='Compute Sheet']")
    confirm_btn = (By.XPATH, "//span[text()='Confirm']")
    refund_btn = (By.XPATH, "//span[text()='Refund']")
    OK = "//span[text()='Ok']"
    save = (By.XPATH, "//button[text()[normalize-space()='Save']]")
    edit = (By.XPATH, "//button[text()[normalize-space()='Edit']]")

    all_emp_names = '//td[@class="o_data_cell o_required_modifier"][1]'
    action_btn = (By.XPATH, "//button[text()[normalize-space()='Action']]")
    delete_btn = (By.XPATH, "//a[text()[normalize-space()='Delete']]")

    def __init__(self, driver):
        super().__init__(driver)

    def generate_payslip(self, emp_name, from_date, to_date, structure, sheet_name, rownum):

        try:
            time.sleep(5)
            self.click(self.create)
            self.wait_till_click(self.save)
            self.click(self.employee_dropdown)
            self.click(self.search_more)
            self.select_from_table(self.all_emp, emp_name)
            self.click(self.from_date)
            self.select_date(from_date)
            self.click(self.to_date)
            self.select_date(to_date)
            self.click(self.structure_dropdown)
            self.select_from_table(self.all_structure, structure)
            self.click(self.save)
            time.sleep(5)
            try:
                if self.get_element(self.OK).is_displayed():
                    ScreenShot.takeScreenshot(self.driver, 'Error while creating payroll ')
                    self.get_element(self.OK).click()
            except NoSuchElementException:
                pass
            time.sleep(5)

            pay_slip = self.getText(self.pay_slip_name)

            assert pay_slip + " - Odoo" == self.driver.title
            ScreenShot.takeScreenshot(self.driver, pay_slip)
            if rownum != 0:
                ExcelUtil.write_data(PropertyFile.getValues('test_report_file'),
                                     sheet_name, rownum, 6,
                                     "payroll created successfully ")
                ExcelUtil.write_data(PropertyFile.getValues('test_report_file'),
                                     sheet_name, rownum, 7,
                                     'Pass')
            return EmployeesPage.EmployeePage(self.driver)

        except Exception:

            if rownum != 0:
                ExcelUtil.write_data(PropertyFile.getValues('test_report_file'),
                                     sheet_name, rownum, 6,
                                     "Error while adding payroll ")
                ExcelUtil.write_data(PropertyFile.getValues('test_report_file'),
                                     sheet_name, rownum, 7,
                                     'Pass')
            return None

    def delete_payslip(self, empName):
        time.sleep(5)
        self.select_from_table(self.all_emp_names, empName)
        self.click(self.action_btn)
        self.click(self.delete_btn)
        time.sleep(5)
        try:
            if self.get_element(self.OK).is_displayed():
                ScreenShot.takeScreenshot(self.driver, 'deletion of payslip')
                self.get_element(self.OK).click()
        except NoSuchElementException:
            pass
        time.sleep(5)
        return "success"

