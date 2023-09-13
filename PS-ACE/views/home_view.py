from appium.webdriver.common.mobileby import MobileBy
from views.base_view import BaseView
from time import sleep,time
from lib.hs_logger import logger
from views.availability_view import AvailabilityView
from views.exchange_view import ExchangeView
from views.search_view import SearchView
from views.search_view import SearchViewIOS
from views.availability_view import AvailabilityViewIOS
from views.exchange_view import ExchangeViewIOS
class HomeView(BaseView):

    def __init__(self,driver,session_data):
        super().__init__(driver,session_data)
        
        self.SKIP_BUTTON = (MobileBy.ID, 'com.flipkart.android:id/custom_back_icon')
        self.LANGUAGE_SELECTION_BUTTON = (MobileBy.XPATH, '//android.widget.TextView[@text="English"]')
        self.HOME_PAGE_LOAD = (MobileBy.XPATH,'//android.widget.TextView[@text="Brand Mall"]')
        
    def nav_to_home_page(self):
        self.session_data.status = "Fail_verfiy_Home_page_lodaded"
        self.session_data.non_time_kpis['home_page_launched'] = "False"
        self.session_data.kpi_labels['home_page_load_time'] = {'start': None, 'end': None}
        self.session_data.kpi_labels['home_page_load_time']['start'] = int(round(time() * 1000))
        self.launchapp()
        logger.info('APP Launched')
        self.wait_for(self.SKIP_BUTTON).click()
        self.wait_for_visibility(self.HOME_PAGE_LOAD)
        self.session_data.kpi_labels['home_page_load_time']['end'] = int(round(time() * 1000))
        self.session_data.non_time_kpis['home_page_launched'] = "True"
        #self.wait_for(self.LANGUAGE_SELECTION_BUTTON).click()
        logger.info('Home page Loaded')


class HomeViewIOS(HomeView):

    #print("IOS")

    def __init__(self,driver,session_data):
        super().__init__(driver,session_data)
        self.HOME_PAGE_LOAD = (MobileBy.ACCESSIBILITY_ID,'Brand Mall')
        
    def nav_to_home_page(self):
        self.session_data.status = "Fail_verfiy_Home_page_lodaded"
        self.session_data.non_time_kpis['home_page_launched'] = "False"
        self.session_data.kpi_labels['home_page_load_time'] = {'start': None, 'end': None}
        self.session_data.kpi_labels['home_page_load_time']['start'] = int(round(time() * 1000))
        self.launchapp()
        logger.info('APP Launched')
        self.wait_for_visibility(self.HOME_PAGE_LOAD)
        self.session_data.kpi_labels['home_page_load_time']['end'] = int(round(time() * 1000))
        self.session_data.non_time_kpis['home_page_launched'] = "True"
        logger.info('Home page Loaded')



        
        
        






