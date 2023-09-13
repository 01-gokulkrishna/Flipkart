from appium.webdriver.common.mobileby import MobileBy
import time

from views.base_view import BaseView

class VideoView(BaseView):
    
    def __init__(self,driver,session_data):
        super().__init__(driver,session_data)

        self.VIDEO_TAB=(MobileBy.XPATH,"//android.widget.CompoundButton[@text='Videos']")
        self.VIDEO_TAB_ELEMENT=(MobileBy.ACCESSIBILITY_ID,"Post options")
        self.VIDEO_ELEMENT=(MobileBy.XPATH,"(//android.widget.TextView[@text='Previously live'])[1]")
        self.VIDEO_PLAYING_ELEMENT=(MobileBy.ACCESSIBILITY_ID,"Send")
        self.LIKE_BUTTON=(MobileBy.ID,"com.linkedin.android:id/media_viewer_react_button")

    def video_function(self):

        print("Video tab")

        self.session_data.status = "Fail_to_open_video_tab"

        self.session_data.non_time_kpis['video_tab_launched'] = "False"
        self.session_data.kpi_labels['video_tab_load_time'] = {'start': None, 'end': None}
        
        self.session_data.kpi_labels['video_tab_load_time']['start'] = int(round(time.time() * 1000))
        self.wait_for(self.VIDEO_TAB).click()
        self.wait_for(self.VIDEO_TAB_ELEMENT)
    
        self.session_data.kpi_labels['video_tab_load_time']['end'] = int(round(time.time() * 1000))

        self.session_data.non_time_kpis['video_tab_launched'] = "True"

        
        while True:
            try:
                if(self.wait_for(self.VIDEO_ELEMENT).is_displayed()): 
                    
                    self.session_data.status = "Fail_to_open_posts_tab"

                    self.session_data.non_time_kpis['video_launched'] = "False"
                    self.session_data.kpi_labels['video_load_time'] = {'start': None, 'end': None}

                    self.session_data.kpi_labels['video_load_time']['start'] = int(round(time.time() * 1000))
                    
                    print("Entered into the video_load_time kpi")
                    self.wait_for(self.VIDEO_ELEMENT).click()
                    self.wait_for(self.VIDEO_PLAYING_ELEMENT)
                    
                    self.session_data.kpi_labels['video_load_time']['end'] = int(round(time.time() * 1000))

                    self.session_data.non_time_kpis['video_launched'] = "True" 

                    break
            except:
                self.scroll(532,1664,532,1116)
        
        self.short_wait_for(self.LIKE_BUTTON).click()
        self.Back()
        

class VideoViewIOS(VideoView):

    def __init__(self,driver,session_data):
        super().__init__(driver,session_data)
        self.VIDEOS_TAB_IOS=(MobileBy.XPATH,"//XCUIElementTypeStaticText[@value='Videos']")
        self.VIDEO_ELEMENT_IOS=(MobileBy.XPATH,"(//XCUIElementTypeOther[@name='urn:li:fs_updateV2:(urn:li:activity:7095037116455256064,COMPANY_VIDEOS,EMPTY,DEFAULT,false)LINFeedPresenterStackCardView'])[2]")
        self.MUTE_BUTTON=(MobileBy.XPATH,"//XCUIElementTypeButton[@label='Mute']")
        self.CLOSE_BUTTON=(MobileBy.XPATH,"//XCUIElementTypeButton[@label='Close']")
        self.RECAT_BUTTON=(MobileBy.XPATH,"//XCUIElementTypeButton[contains(@label,'React')]")
        self.BACK_BUTTON=(MobileBy.XPATH,"(//XCUIElementTypeButton[contains(@label,'Back')])[1]")
        self.BACK_IOS=(MobileBy.XPATH,"//XCUIElementTypeButton[@label='Back']")


    def video_function(self):

        print("Video Tab")

        self.session_data.status = "Fail_to_open_video_tab"

        self.session_data.non_time_kpis['video_tab_launched'] = "False"
        self.session_data.kpi_labels['video_tab_load_time'] = {'start': None, 'end': None}
        
        self.session_data.kpi_labels['video_tab_load_time']['start'] = int(round(time.time() * 1000))
        self.wait_for(self.VIDEOS_TAB_IOS).click()
    
        self.session_data.kpi_labels['video_tab_load_time']['end'] = int(round(time.time() * 1000))

        self.session_data.non_time_kpis['video_tab_launched'] = "True"
    
        time.sleep(2)

        self.session_data.status = "Fail_to_open_video_tab"

        self.session_data.non_time_kpis['video_launched'] = "False"
        self.session_data.kpi_labels['video_load_time'] = {'start': None, 'end': None}

        while True:
            print("In Loop")
            
            
            self.session_data.kpi_labels['video_load_time']['start'] = int(round(time.time() * 1000))
            try:
               
                self.scroll(208,710,208,710)
                print("Element clicked waiting fo mute button")

                if(self.short_wait_for(self.MUTE_BUTTON).is_displayed()):
                    print("Mute button displayed ")

                    self.session_data.kpi_labels['video_load_time']['end'] = int(round(time.time() * 1000))

                    self.session_data.non_time_kpis['video_launched'] = "True"

                    self.short_wait_for(self.RECAT_BUTTON).click()
                    print("reacted")
                    break
                    
            except:
                # print("Outer except block")
                
                try:
                    if(self.short_wait_for(self.CLOSE_BUTTON).is_displayed()):
                        self.short_wait_for(self.CLOSE_BUTTON).click()
                        # print("close button clicked")
                except:
                    # print("Comes to inmner except")
                    self.short_wait_for(self.BACK_IOS).click()

                self.scroll(218,555,219,411)
        
        self.short_wait_for(self.BACK_BUTTON).click()

                
        




