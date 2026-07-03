from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def _get_product_button_locator(self, product_name):
        """Generates the direct button XPath."""
        xpath = (
            f"//div[contains(@class, 'inventory_item')]"
            f"[.//div[contains(@class, 'inventory_item_name') and normalize-space()='{product_name}']]"
            f"//button"
        )
        return (By.XPATH, xpath)

    def click_add_to_cart(self, product_name):
        """Clicks 'Add to Cart' using JS instantly."""
        button_locator = self._get_product_button_locator(product_name)
        # Fast grab: find_element happens instantly if it's there
        button = self.driver.find_element(*button_locator)
        self.driver.execute_script("arguments[0].click();", button)

    def click_remove_from_cart(self, product_name):
        """Clicks 'Remove' using JS instantly."""
        button_locator = self._get_product_button_locator(product_name)
        button = self.driver.find_element(*button_locator)
        self.driver.execute_script("arguments[0].click();", button)
    
    def get_cart_count(self):
        """Retrieves current item count with zero artificial delays."""
        badges = self.driver.find_elements(*self.SHOPPING_CART_BADGE)
        if len(badges) > 0:
            return int(badges[0].text)
        return 0