from appium.webdriver.common.mobileby import MobileBy
from time import sleep,time
from lib.hs_logger import logger
from views.base_view import BaseView
class SearchView(BaseView):

    def __init__(self,driver,session_data):
        super().__init__(driver,session_data)
        self.CATEGORIES_BUTTON= (MobileBy.XPATH, '//android.widget.TextView[@text="Categories"]')
        self.SEARCH_BOX = (MobileBy.ID, 'com.flipkart.android:id/search_icon')
        ##self.SEARCH_BOX = (MobileBy.XPATH, '//android.widget.TextView[@text="Search for products"]')
        self.SEARCH_PRODUCT = (MobileBy.XPATH, '//android.widget.EditText[@text="Search for products"]')
        self.SELECT_OPTION = (MobileBy.XPATH, '//android.widget.TextView[@text="vivo v29e"]')
        self.NOT_NOW_BUTTON = (MobileBy.ID, 'com.flipkart.android:id/not_now_button')
        self.DEVICE = (MobileBy.XPATH, '//android.widget.TextView[@text="vivo V29e 5G (Artistic Red, 256 GB)"]')                                               
        self.DEVICE_DETAIL_PAGE_LOAD = (MobileBy.XPATH,'//android.widget.TextView[@text="Select Variant"]')

    def search(self):
        self.session_data.status = "Fail_Search"
        self.wait_for(self.CATEGORIES_BUTTON).click()
        self.wait_for(self.SEARCH_BOX).click()
        self.wait_for(self.SEARCH_PRODUCT).send_keys('Vivo v29e')#('SAMSUNG Galaxy S23 Ultra')
        self.session_data.non_time_kpis['Smart_phone_gridwall'] = "False"
        self.session_data.kpi_labels['Smart_phone_gridwall'] = {'start': None, 'end': None}
        self.session_data.kpi_labels['Smart_phone_gridwall']['start'] = int(round(time() * 1000))
        self.wait_for(self.SELECT_OPTION).click()
        logger.info('Search Done')
        self.wait_for(self.NOT_NOW_BUTTON).click()
        self.wait_for_visibility(self.DEVICE)
        self.session_data.kpi_labels['Smart_phone_gridwall']['end'] = int(round(time() * 1000))
        self.session_data.non_time_kpis['Smart_phone_gridwall'] = "True"
        
        
        self.session_data.non_time_kpis['Device_Details'] = "False"
        self.session_data.kpi_labels['Device_Details'] = {'start': None, 'end': None}
        self.session_data.kpi_labels['Device_Details']['start'] = int(round(time() * 1000))
        self.wait_for(self.DEVICE).click()
        self.wait_for_visibility(self.DEVICE_DETAIL_PAGE_LOAD)
        self.session_data.kpi_labels['Device_Details']['end'] = int(round(time() * 1000))
        self.session_data.non_time_kpis['Device_Details'] = "True"
        logger.info('Device Selected')
        

class SearchViewIOS(SearchView):
    def __init__(self,driver,session_data):
        super().__init__(driver,session_data)
        self.CATEGORIES_BUTTON= (MobileBy.ACCESSIBILITY_ID,'Categories')
        self.SEARCH_BOX = (MobileBy.XPATH, '//XCUIElementTypeOther[@name="Search for products"]')
        self.SELECT_OPTION = (MobileBy.XPATH, '//XCUIElementTypeOther[@name="vivo v29e in Mobiles"]')
        self.SELECT_OPTION_1 = (MobileBy.XPATH, '//XCUIElementTypeOther[@name="vivo v29 e mobiles in Mobiles"]')
        self.DEVICE = (MobileBy.XPATH, '//XCUIElementTypeOther[contains(@name, "vivo V29e 5G (Artistic Red, 256 GB) ")]')   
        self.GOT_IT_BUTTON= (MobileBy.ACCESSIBILITY_ID,'Got it')                                              
        self.DEVICE_DETAIL_PAGE_LOAD = (MobileBy.XPATH,'//XCUIElementTypeStaticText[@name="Select Variant"]')
        
    def search(self):
        self.session_data.status = "Fail_Search"
        self.wait_for_elements(self.SEARCH_BOX)[1].click()
        self.wait_for_elements(self.SEARCH_BOX)[-1].send_keys('vivo v29e')
        self.session_data.non_time_kpis['Smart_phone_gridwall'] = "False"
        self.session_data.kpi_labels['Smart_phone_gridwall'] = {'start': None, 'end': None}
        self.session_data.kpi_labels['Smart_phone_gridwall']['start'] = int(round(time() * 1000))
        try:
            self.wait_for_elements(self.SELECT_OPTION)[-1].click()
        except:
            self.wait_for_elements(self.SELECT_OPTION_1)[-1].click()
        logger.info('Search Done')
        self.wait_for_visibility(self.DEVICE)
        self.session_data.kpi_labels['Smart_phone_gridwall']['end'] = int(round(time() * 1000))
        self.session_data.non_time_kpis['Smart_phone_gridwall'] = "True"

        self.session_data.non_time_kpis['Device_Details'] = "False"
        self.session_data.kpi_labels['Device_Details'] = {'start': None, 'end': None}
        self.session_data.kpi_labels['Device_Details']['start'] = int(round(time() * 1000))
        self.wait_for(self.DEVICE).click()
        self.wait_for_visibility(self.DEVICE_DETAIL_PAGE_LOAD)
        self.session_data.kpi_labels['Device_Details']['end'] = int(round(time() * 1000))
        self.session_data.non_time_kpis['Device_Details'] = "True"
        logger.info('Device Selected')



