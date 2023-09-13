from appium.webdriver.common.mobileby import MobileBy
from time import sleep,time
from views.base_view import BaseView
from lib.hs_logger import logger

class ExchangeView(BaseView):

    def __init__(self,driver,session_data):
        super().__init__(driver,session_data)

        self.CANCEL_EXCHANGE_BUTTON = (MobileBy.XPATH, '//android.widget.TextView[@text="Cancel Exchange "]')
        self.YES_BUTTON = (MobileBy.XPATH, '//android.widget.TextView[@text="Yes"]')
        self.APPLY_BUTTON = ((MobileBy.XPATH, '//android.widget.TextView[@text="Apply "]'))
        self.CONTINUE_BUTTON =  (MobileBy.XPATH, '//android.widget.TextView[@text="Continue "]')
        self.DEVICE_CONDITION = (MobileBy.XPATH, '//android.widget.ImageView[@text=""]')
        self.CONFIRM_BUTTON = (MobileBy.XPATH, '//android.widget.TextView[@text="Confirm Exchange "]')
        self.GET_PRICE = (MobileBy.XPATH, '//android.widget.TextView[contains(@text, "Exchange Applied")]')
        self.FINISH = (MobileBy.XPATH,'//android.widget.TextView[@text="Select Variant"]')

    def nav_check_exchange(self):
        self.session_data.status = "Fail_Exchange" 
        sleep(2)
        self.swipe(2500)
        logger.info('Exchange Started')
        try:
            self.wait_for(self.CANCEL_EXCHANGE_BUTTON).click()
            self.wait_for(self.YES_BUTTON).click()
            sleep(3)
        except:
            pass
        self.session_data.non_time_kpis['Exchange_time'] = "False"
        self.session_data.kpi_labels['Exchange_time'] = {'start': None, 'end': None} 
        self.session_data.kpi_labels['Exchange_time']['start'] = int(round(time() * 1000))
        self.wait_for(self.APPLY_BUTTON).click()
        #self.wait_for_elements(self.DEVICE_CONDITION)[1].click()
        self.wait_for(self.CONFIRM_BUTTON).click()
        self.wait_for_visibility(self.FINISH)
        self.session_data.kpi_labels['Exchange_time']['end'] = int(round(time() * 1000))
        self.session_data.non_time_kpis['Exchange_time'] = "True"

        logger.info('Exchange Finished')
        #print('Exchange price')
        sleep(2)
        #self.swipe(75)
        #print(self.wait_for(self.GET_PRICE).text)
        self.session_data.status = 'Pass'

class ExchangeViewIOS(ExchangeView):

    def __init__(self,driver,session_data):
        
        super().__init__(driver,session_data)

        self.CANCEL_EXCHANGE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Cancel Exchange ')
        self.YES_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeOther[@name="Yes"]')
        self.APPLY_BUTTON =  (MobileBy.ACCESSIBILITY_ID, 'Apply ')
        self.CONFIRM_BUTTON = (MobileBy.XPATH, '//android.widget.TextView[@text="Confirm Exchange "]')
        self.GET_PRICE = (MobileBy.XPATH, '//android.widget.TextView[contains(@text, "Exchange Applied")]')

    def nav_check_exchange(self): 
        sleep(2)
        self.swipe(2500)
        logger.info('Exchange Started')
        try:
            self.wait_for(self.CANCEL_EXCHANGE_BUTTON).click()
            self.wait_for_elements(self.YES_BUTTON)[1].click()
            sleep(3)
        except:
            pass
        
        self.session_data.non_time_kpis['Exchange_time'] = "False"
        self.session_data.kpi_labels['Exchange_time'] = {'start': None, 'end': None} 
        self.session_data.kpi_labels['Exchange_time']['start'] = int(round(time() * 1000))
        self.wait_for(self.APPLY_BUTTON).click()
        #self.wait_for_elements(self.DEVICE_CONDITION)[1].click()
        #self.wait_for(self.CONFIRM_BUTTON).click()
        self.tap()
        self.session_data.kpi_labels['Exchange_time']['end'] = int(round(time() * 1000))
        self.session_data.non_time_kpis['Exchange_time'] = "True"
        logger.info('Exchange Finished')
        #print('Exchange price')
        sleep(2)
        #self.swipe(75)
        #print(self.wait_for(self.GET_PRICE).text)
        self.session_data.status = 'Pass'






    '''def goto_post_page(self):
        PostPageObject = PostsView.instance(self.driver,self.session_data)
        return PostPageObject

'''


    
