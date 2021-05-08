from Pages.BasePage import BasePage
from Pages.DepartmentPage import DepartmentPage
from Pages.EmployeesPage import EmployeePage
from Pages.PayrollPage import PayrollPage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    user_menu = (By.XPATH, "(//li[@class='o_user_menu']//a)[1]")
    app_list = (By.CLASS_NAME, "full")

    employee_app = (By.LINK_TEXT, "Employees")
    employee_txt = (By.XPATH, "//li[text()='Employees']")

    department_menu = (By.LINK_TEXT, "Departments")
    departments_txt = (By.XPATH, "// li[text() = 'Departments']")

    employee_menu = (By.LINK_TEXT, "Employees")

    payroll_app = (By.LINK_TEXT, "Payroll")
    payroll_txt = (By.XPATH, "//li[text()='Employee Payslips']")

    logout_btn = (By.XPATH, "//a[@data-menu='logout']")
    OK = "//span[text()='Ok']"

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_employees_app(self):
        self.click(self.app_list)
        self.click(self.employee_app)
        self.wait_till_presence(self.employee_txt)
        return EmployeePage(self.driver)

    def navigate_to_add_employee(self):
        self.click(self.employee_menu)
        self.wait_till_presence(self.employee_txt)
        return EmployeePage(self.driver)

    def navigate_to_app_department(self):
        self.click(self.department_menu)
        self.wait_till_presence(self.departments_txt)
        return DepartmentPage(self.driver)

    def navigate_to_payroll_app(self):
        self.click(self.app_list)
        self.click(self.payroll_app)
        self.wait_till_presence(self.payroll_txt)
        return PayrollPage(self.driver)

    def do_logout(self):
        self.click(self.user_menu)
        self.click(self.logout_btn)
        try:
            if self.get_element(self.OK).is_displayed():
               self.get_element(self.OK).click()
        except Exception:
            pass
