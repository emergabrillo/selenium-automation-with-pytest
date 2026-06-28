from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators for the login page elements
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "submit")
    ERROR_MESSAGE = (By.ID, "error")

    def enter_username(self, username):
        """Enters the username into the username input field."""
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Enters the password into the password input field."""
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Clicks the login button to submit the form."""
        self.click_element(self.SUBMIT_BUTTON)

    def get_error_message(self):
        """Retrieves the error message displayed on the login page, once displayed."""
        try:
            error_element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
            return error_element.text  # Returns the text of the error message if present
        except:
            return None  # Returns None if no error message is found