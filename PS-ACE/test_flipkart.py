from views.home_view import HomeView
from views.availability_view import AvailabilityView
from views.search_view import SearchView
from views.exchange_view import ExchangeView
import time

class TestFlipkart:
    
    package="com.flipkart.android"
    activity=".activity.HomeFragmentHolderActivity"
    test_name="Flipkart_test"
    bundle_id= "com.appflipkart.flipkart"
    

    def test_flipkart(self,driver):
        home = HomeView.instance(driver,self.session_data)
        home.nav_to_home_page()

        search = SearchView.instance(driver,self.session_data)
        search.search()

        availability = AvailabilityView.instance(driver,self.session_data)
        availability.nav_check_availability()

        exchange = ExchangeView.instance(driver,self.session_data)
        exchange.nav_check_exchange()
        