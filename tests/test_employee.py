import pytest
from Pages.LoginPage import LoginPage
from testData.TestData import TestData
from utilities.BaseClass import BaseClass


class TestEmployee(BaseClass):

    @pytest.mark.order(1)
    def test_employee(self, getData):
        driver = self.driver
        logger = self.getLogger()

        loginpage = LoginPage(driver)

        homepage = loginpage.do_login(BaseClass.login_email, BaseClass.login_password, " ", 0)
        if homepage is not None:
            logger.info('Logged In Successfully')
        result = homepage.navigate_to_employees_app()
        if result is not None:
            logger.info('navigated to employees app')

        emppage = homepage.navigate_to_add_employee()
        payrollpage = emppage.add_a_employee(getData['employee_name'],
                                             getData['employee_type'],
                                             getData['work_address'],
                                             getData['work_loc'],
                                             getData['email'],
                                             getData['mobile'],
                                             getData['dept'],
                                             getData['job_position'],
                                             getData['manager'],
                                             getData['sheet_name'],
                                             getData['rowNum'])
        if payrollpage is not None:
            logger.info('one employee added successfully')
        logout = homepage.do_logout()
        if logout is not None:
            logger.info('successfully logged out')

    @pytest.fixture(params=TestData.getTestData('Test_data_for_employee'))
    def getData(self, request):
        return request.param
