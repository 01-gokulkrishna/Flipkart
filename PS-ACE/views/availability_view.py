from appium.webdriver.common.mobileby import MobileBy
from time import sleep,time
from lib.hs_logger import logger
from views.base_view import BaseView
#from views.exchange_view import ExchangeView



class AvailabilityView(BaseView):
    def __init__(self,driver,session_data):
        super().__init__(driver,session_data)
        self.PINCODE_SEARCH_BOX = (MobileBy.XPATH, '//android.widget.TextView[@text="Enter pincode "]')
        self.CHANGE_BUTTON = (MobileBy.XPATH, '//android.widget.TextView[@text="Change "]')
        self.PINCODE_TEXT_BOX= (MobileBy.XPATH, '//android.widget.EditText[@text="Enter pincode"]')
        self.SUBMIT_BUTTON = (MobileBy.XPATH, '//android.widget.TextView[@text="Submit "]')
        self.LOCATION = (MobileBy.XPATH, '//android.widget.TextView[@text="Kozhikode - 673005"]')
    def nav_check_availability(self):
        self.session_data.status = "Fail_Availability_Check"
        #sleep(2)
        self.swipe(1000)
        logger.info('Started Availability Check')
        try:
            self.wait_for(self.CHANGE_BUTTON).click()
        except:
            self.wait_for(self.PINCODE_SEARCH_BOX).click()
        self.wait_for(self.PINCODE_TEXT_BOX).send_keys('673005')
        self.session_data.non_time_kpis['Availability_Search_time'] = "False"
        self.session_data.kpi_labels['Availability_Search_time'] = {'start': None, 'end': None}
        self.session_data.kpi_labels['Availability_Search_time']['start'] = int(round(time() * 1000))
        self.wait_for(self.SUBMIT_BUTTON).click()
        self.wait_for_visibility(self.LOCATION)
        self.session_data.kpi_labels['Availability_Search_time']['end'] = int(round(time() * 1000))
        self.session_data.non_time_kpis['Availability_Search_time'] = "True"
        logger.info(' Finished Availability Check')
        #sleep(2)


class AvailabilityViewIOS(AvailabilityView):

    def __init__(self,driver,session_data):
        
        super().__init__(driver,session_data)
        self.PINCODE_SEARCH_BOX = (MobileBy.ACCESSIBILITY_ID, 'Enter pincode ')
        self.CHANGE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Change ')
        self.PINCODE = (MobileBy.XPATH, '//XCUIElementTypeTextField[@value="Enter pincode"]')
        self.SUBMIT = (MobileBy.XPATH, '(//XCUIElementTypeOther[@name="Submit "])[3]')
        self.LOCATION = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Kozhikode - 673005"]')
    def nav_check_availability(self):
        self.session_data.status = "Fail_Availability_Check"
        sleep(2)
        self.swipe(1000)
        logger.info('Started Availability Check')
        try:
            self.wait_for(self.CHANGE_BUTTON).click()
        except:
            self.wait_for(self.PINCODE_SEARCH_BOX).click()
        self.wait_for(self.PINCODE).send_keys('673005')
        self.session_data.non_time_kpis['Availability_Search_time'] = "False"
        self.session_data.kpi_labels['Availability_Search_time'] = {'start': None, 'end': None}
        self.session_data.kpi_labels['Availability_Search_time']['start'] = int(round(time() * 1000))
        self.wait_for(self.SUBMIT).click()
        self.wait_for_visibility(self.LOCATION)
        self.session_data.kpi_labels['Availability_Search_time']['end'] = int(round(time() * 1000))
        self.session_data.non_time_kpis['Availability_Search_time'] = "True"
        logger.info(' Finished Availability Check')
        sleep(2)



