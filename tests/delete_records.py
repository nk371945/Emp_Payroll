import pytest

from Pages.LoginPage import LoginPage
from utilities import PropertyFile
from utilities.BaseClass import BaseClass


class TestPostProcess(BaseClass):

    @pytest.mark.order(1)
    def test_deletion(self):
        driver = self.driver
        logger = self.getLogger()
        name = PropertyFile.getValues('name')
        loginpage = LoginPage(driver)

        homepage = loginpage.do_login(BaseClass.login_email, BaseClass.login_password, " ", 0)
        if homepage is not None:
            logger.info('Logged In Successfully')
            payrollpage = homepage.navigate_to_payroll_app()
            if payrollpage is not None:
                logger.info('Navigated to payroll')
                result = payrollpage.delete_payslip(name)
                if result is not None:
                    logger.info('payslip deleted')

            emppage = homepage.navigate_to_employees_app()
            if emppage is not None:
                logger.info('Navigated to employee')
                rs = emppage.delete_employee(name)
                if rs is not None:
                    logger.info('employee profile deleted')

            homepage.do_logout()
            logger.info('Logged Out Successfully')
        else:
            logger.info('Logged In Unsuccessful')

