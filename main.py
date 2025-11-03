import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urban_routes_page import UrbanRoutesPage


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code



class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_complete_taxi_order(self):
        """Test the complete taxi ordering process"""
        # Initialize the page
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        
        # 1. Set route
        routes_page.set_route(data.address_from, data.address_to)
        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to

        # 2. Select Comfort taxi
        routes_page.select_comfort_taxi()

        # 3. Enter phone number
        routes_page.enter_phone_number(data.phone_number)
        code = retrieve_phone_code(self.driver)
        routes_page.enter_confirmation_code(code)

        # 4. Add credit card
        routes_page.add_credit_card(data.card_number, data.card_code)

        # 5. Write message for driver
        routes_page.write_message_for_driver(data.message_for_driver)

        # 6. Request blanket and tissues
        routes_page.request_blanket_and_tissues()

        # 7. Request ice cream
        routes_page.request_ice_cream(2)

        # 8. Submit order and verify search starts
        routes_page.submit_order()
        assert routes_page.is_searching_for_taxi(), "Taxi search modal did not appear"

        # 9. Optional: Wait for driver info
        try:
            routes_page.wait_for_driver_info()
        except:
            print("Note: Driver information did not appear within the timeout period")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
