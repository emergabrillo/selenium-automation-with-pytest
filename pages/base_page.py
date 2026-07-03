from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Safe 10-second explicit wait window

    def click_element(self, locator):
        """Waits for an element to be clickable before interacting."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        """Waits for visibility, clears existing inputs, and types text safely."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_element(self, locator, timeout=10):
        """Waits for an element to be visible and retrieves it. Dynamic timeout allows for flexible waits."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element