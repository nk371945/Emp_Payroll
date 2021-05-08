import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver


from utilities import PropertyFile

driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.get(PropertyFile.getValues('url'))
    driver.maximize_window()
    request.cls.driver = driver
    yield

    # Close browser window:
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    # print('*****', outcome, '*****')
    # print('*****', rep.nodeid, '*****')
    # print('*****', rep.location, '*****')
    # print('*****', item, '*****')
    # print('*****', call, '*****')

    if rep.outcome == 'failed':
        allure.attach(driver.get_screenshot_as_png(), name=rep.nodeid, attachment_type=AttachmentType.PNG)
    # setattr(item, "rep_" + rep.when, rep)
    # return rep
