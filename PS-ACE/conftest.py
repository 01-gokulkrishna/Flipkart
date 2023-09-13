import pytest
import sys
import time
import logging
import json
import os
import importlib
from appium import webdriver

root_dir = os.path.dirname(__file__)
lib_dir = os.path.join(root_dir, 'lib')
views_dir = os.path.join(root_dir, 'views')
sys.path.append(lib_dir)
sys.path.append(views_dir)
from hs_api import hsApi
from args_lib import addoption, init_args
import pytest_sample_lib
from hs_logger import logger, setup_logger
import session_visual_lib
setup_logger(logger, logging.DEBUG)
session_data = None

# Command line args are defined here
def pytest_addoption(parser):
    addoption(parser)

@pytest.fixture
def driver(request):

    global session_data
    session_data = request.cls
    session_data = init_args(request, session_data)
    pytest_sample_lib.init_timing(session_data)
    session_data.status = "Fail_creating_driver"
    driver = webdriver.Remote(
        command_executor=session_data.appium_input,
        desired_capabilities=session_data.desired_caps
    )
    logger.info("Starting Driver")
    # Get Device
    r = driver.session
    session_data.udid = r['udid']
    if driver.capabilities['platformName'].lower() =="android":
        device_model = r['deviceModel']
    else:
        device_model = r['device']
    logger.info("Running test on " + device_model +":" + session_data.udid)
    # creating a object of hs_api for future use of headspin api calls
    session_data.hs_api_call = hsApi(session_data.udid, session_data.access_token)
    session_data.session_id = driver.session_id

    request.cls.session_data = session_data
    yield driver
    tearDown(session_data, driver)


def tearDown(session_data, driver):
    
    if session_data.status != 'Pass':
        page_source = driver.page_source
        # print('failed page_source')
        # print(page_source)
    try:
        driver.terminate_app(session_data.package)
    finally:
        driver.quit()
    time.sleep(3)
        
    logger.info("https://ui-dev.headspin.io/sessions/" + session_data.session_id + "/waterfall")
    
    if session_data.use_capture:
        session_visual_lib.run_record_session_info(session_data)

        