import pytest
from Pages.LoginPage import LoginPage
from testData.TestData import TestData
from utilities.BaseClass import BaseClass


class TestPayroll(BaseClass):

    @pytest.mark.order(1)
    def test_payroll(self, getData):
        driver = self.driver
        logger = self.getLogger()

        loginpage = LoginPage(driver)

        homepage = loginpage.do_login(BaseClass.login_email, BaseClass.login_password, " ", 0)
        if homepage is not None:
            logger.info('Logged In Successfully')
        payrollpage = homepage.navigate_to_payroll_app()
        if payrollpage is not None:
            logger.info('navigated to payroll app')

        emppage = payrollpage.generate_payslip(getData['emp_name'],
                                               getData['from_date'],
                                               getData['to_date'],
                                               getData['structure'],
                                               getData['sheet_name'],
                                               getData['rowNum'])

        if emppage is not None:
            logger.info('payslip is generated successfully')
        homepage.do_logout()

        logger.info('Logged Out Successfully')

    @pytest.fixture(params=TestData.getTestData('Test_data_for_payroll'))
    def getData(self, request):
        return request.param
