import time
import importlib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton
from appium.webdriver.common.touch_action import TouchAction

from lib.hs_logger import logger

def class_for_name(module_name, class_name):
    """ This is a helper method to get a class reference dynamically """
    dir_name = importlib.import_module(module_name)
    print(dir_name)
    return getattr(dir_name, class_name)

class BaseView(object):
    def __init__(self , driver, session_data):
        self.driver = driver
        self.session_data = session_data
        self.wait = WebDriverWait(self.driver, 30)
        self.wait_short = WebDriverWait(self.driver, 5)
        self.wait_long = WebDriverWait(self.driver, 80)
        self.wait_long_double = WebDriverWait(self.driver, 120)
        

        self.NAVIGATE_BACK=(MobileBy.ACCESSIBILITY_ID,"Back")
        
    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def short_wait_for(self,locator):
        return self.wait_short.until(EC.presence_of_element_located(locator))
    
    def wait_for_all(self,locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))
    
    def short_wait_for_invisibility(self, locator):
        return self.wait_short.until(EC.invisibility_of_element_located(locator))

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))    

    def short_wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))      

    def long_wait_for(self, locator):
        return self.wait_long.until(EC.presence_of_element_located(locator))

    def long_double_wait_for(self, locator):
        return self.wait_long_double.until(EC.presence_of_element_located(locator))

    def short_wait_for_elements(self, locator):
        return self.wait_short.until(EC.presence_of_all_elements_located(locator))

    def wait_for_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def long_wait_for_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def long_wait_for_clickable(self, locator):
        return self.wait_long.until(EC.element_to_be_clickable(locator))

    def short_wait_for(self, locator):
        return self.wait_short.until(EC.presence_of_element_located(locator))

    def short_wait_for_clickable(self, locator):
        return self.wait_short.until(EC.element_to_be_clickable(locator))

    def find(self, locator):
        return self.driver.find_element(*locator)


    def scroll(self,start_x,start_y,end_x,end_y):
        print("Scroll function")
        scroll=ActionBuilder(self.driver)
        finger=scroll.add_pointer_input(POINTER_TOUCH,"finger")
        finger.create_pointer_move(duration=0,x=start_x,y=start_y)
        finger.create_pointer_down(button=MouseButton.LEFT)
        finger.create_pointer_move(duration=300,x=end_x,y=end_y)
        finger.create_pointer_up(MouseButton.LEFT)
        scroll.perform()

    def swipe(self,time):
        screen_width = self.driver.get_window_size()['width']
        screen_height = self.driver.get_window_size()['height']
        start_x = screen_width // 2
        start_y = screen_height * 3 // 4
        end_x = start_x
        end_y = screen_height // 8
        action = TouchAction(self.driver)
        action.press(x=start_x, y=start_y).wait(time).move_to(x=end_x, y=end_y).release().perform()

    def launchapp(self):
        self.driver.launch_app()

    def tap(self):
        action = TouchAction(self.driver)
        x_coordinate = 200  # Replace with the X coordinate you want
        y_coordinate = 830  # Replace with the Y coordinate you want
        action.tap(x=x_coordinate, y=y_coordinate).perform()
        #action.tap(200,830).perform()

    def Back(self):
        for i in range(0,3):
            self.wait_for(self.NAVIGATE_BACK).click()


    @classmethod
    def instance(cls, driver, session_data):
        plat = session_data.os.lower()
        klass = cls.__name__
        if plat == 'ios':
            klass = f'{klass}IOS'
        print(class_for_name('home_view', klass))
        page_object = class_for_name('home_view', klass)(driver, session_data)
        
        return page_object