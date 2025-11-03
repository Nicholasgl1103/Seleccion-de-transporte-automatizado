from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class UrbanRoutesPage:
    # Locators - Fields
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    phone_field = (By.ID, 'phone')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.ID, 'code')
    message_field = (By.ID, 'comment')
    
    # Locators - Buttons and Links
    comfort_taxi = (By.XPATH, "//div[contains(text(), 'Comfort')]")
    payment_method_button = (By.XPATH, "//div[contains(text(), 'Métodos de pago')]")
    add_card_button = (By.XPATH, "//button[contains(text(), 'Agregar una tarjeta')]")
    add_phone_button = (By.CSS_SELECTOR, "div.pp-button.button-blue")
    confirm_phone_button = (By.ID, 'confirm')
    blanket_checkbox = (By.ID, 'blanket')
    tissues_checkbox = (By.ID, 'tissues')
    ice_cream_counter = (By.CSS_SELECTOR, '.counter-plus')
    order_button = (By.XPATH, "//button[contains(text(), 'Pedir un taxi')]")
    
    # Locators - Modal windows and information
    card_modal = (By.CSS_SELECTOR, ".payment-picker_card-form")
    phone_code_modal = (By.CSS_SELECTOR, ".modal")
    search_taxi_modal = (By.CSS_SELECTOR, ".order-body_search")
    driver_info = (By.CSS_SELECTOR, ".order-body_driver")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def set_from(self, from_address):
        """Set the pickup address in the 'from' field"""
        element = self.wait.until(EC.presence_of_element_located(self.from_field))
        element.send_keys(from_address)

    def set_to(self, to_address):
        """Set the destination address in the 'to' field"""
        element = self.wait.until(EC.presence_of_element_located(self.to_field))
        element.send_keys(to_address)

    def get_from(self):
        """Get the text from the 'from' field"""
        element = self.wait.until(EC.presence_of_element_located(self.from_field))
        return element.get_property('value')

    def get_to(self):
        """Get the text from the 'to' field"""
        element = self.wait.until(EC.presence_of_element_located(self.to_field))
        return element.get_property('value')

    def set_route(self, from_address, to_address):
        """Set both pickup and destination addresses"""
        self.set_from(from_address)
        self.set_to(to_address)

    def select_comfort_taxi(self):
        """Select Comfort taxi option"""
        element = self.wait.until(EC.element_to_be_clickable(self.comfort_taxi))
        element.click()

    def enter_phone_number(self, phone):
        """Enter phone number and confirm it"""
        self.wait.until(EC.element_to_be_clickable(self.add_phone_button)).click()
        phone_input = self.wait.until(EC.presence_of_element_located(self.phone_field))
        phone_input.send_keys(phone)
        self.wait.until(EC.element_to_be_clickable(self.add_phone_button)).click()

    def enter_confirmation_code(self, code):
        """Enter phone confirmation code"""
        code_input = self.wait.until(EC.presence_of_element_located(self.confirm_phone_button))
        code_input.send_keys(code)
        code_input.send_keys(Keys.RETURN)

    def add_credit_card(self, card_number, card_code):
        """Add credit card information"""
        # Click on payment method button
        self.wait.until(EC.element_to_be_clickable(self.payment_method_button)).click()
        
        # Click on add card button
        self.wait.until(EC.element_to_be_clickable(self.add_card_button)).click()
        
        # Wait for card modal and fill in details
        self.wait.until(EC.presence_of_element_located(self.card_modal))
        card_number_input = self.wait.until(EC.presence_of_element_located(self.card_number_field))
        card_number_input.send_keys(card_number)
        
        cvv_input = self.wait.until(EC.presence_of_element_located(self.card_code_field))
        cvv_input.send_keys(card_code)
        # Move focus from CVV field by clicking elsewhere
        ActionChains(self.driver).move_to_element(card_number_input).click().perform()

    def write_message_for_driver(self, message):
        """Write a message for the driver"""
        message_input = self.wait.until(EC.presence_of_element_located(self.message_field))
        message_input.send_keys(message)

    def request_blanket_and_tissues(self):
        """Request blanket and tissues"""
        self.wait.until(EC.element_to_be_clickable(self.blanket_checkbox)).click()
        self.wait.until(EC.element_to_be_clickable(self.tissues_checkbox)).click()

    def request_ice_cream(self, quantity=2):
        """Request ice cream"""
        ice_cream_button = self.wait.until(EC.element_to_be_clickable(self.ice_cream_counter))
        for _ in range(quantity):
            ice_cream_button.click()

    def submit_order(self):
        """Submit the taxi order"""
        self.wait.until(EC.element_to_be_clickable(self.order_button)).click()

    def wait_for_driver_info(self):
        """Wait for driver information to appear"""
        return self.wait.until(EC.presence_of_element_located(self.driver_info))

    def is_searching_for_taxi(self):
        """Check if the app is searching for a taxi"""
        return self.wait.until(EC.presence_of_element_located(self.search_taxi_modal)).is_displayed()