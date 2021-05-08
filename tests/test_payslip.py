import pytest
from Pages.LoginPage import LoginPage
from testData.TestData import TestData
from utilities.BaseClass import BaseClass


class TestPaySlip(BaseClass):

    @pytest.mark.order(1)
    def test_payslip(self, getData):
        driver = self.driver
        logger = self.getLogger()

        loginpage = LoginPage(driver)

        homepage = loginpage.do_login(BaseClass.login_email, BaseClass.login_password, " ", 0)
        if homepage is not None:
            logger.info('Logged In Successfully')
        emppage = homepage.navigate_to_employees_app()
        if emppage is not None:
            logger.info('navigated to employee app')

        result = emppage.view_payslip(getData['name'], getData['sheet_name'], getData['rowNum'])
        if result is not None:
            logger.info('payslip downloaded successfully')
        homepage.do_logout()
        logger.info('Logged Out Successfully')

    @pytest.fixture(params=TestData.getTestData('Test_data_for_view_payslip'))
    def getData(self, request):
        return request.param
