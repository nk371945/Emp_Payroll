import pytest
from Pages.LoginPage import LoginPage
from testData.TestData import TestData
from utilities.BaseClass import BaseClass


class TestDepartment(BaseClass):

    @pytest.mark.order(1)
    def test_department(self, getData):
        driver = self.driver
        logger = self.getLogger()

        loginpage = LoginPage(driver)

        homepage = loginpage.do_login(BaseClass.login_email, BaseClass.login_password, " ", 0)
        if homepage is not None:
            logger.info('Logged In Successfully')
        result = homepage.navigate_to_employees_app()
        if result is not None:
            logger.info('navigated to employees app')

        deptpage = homepage.navigate_to_app_department()

        emppage = deptpage.add_a_department(getData['dept_name'], getData['parent_dept_name'], getData['manager_name'], getData['sheet_name'], getData['rowNum'])
        if emppage is not None:
            logger.info('one dept added successfully')

        logout = homepage.do_logout()
        if logout is not None:
            logger.info('successfully logged out')

    @pytest.fixture(params=TestData.getTestData('Test_data_for_department'))
    def getData(self, request):
        return request.param
