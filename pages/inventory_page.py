from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Fixed Locators (Clean and minimal)
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def _get_product_button_locator(self, product_name):
        """Generates a resilient XPath targeting the button for a specific product name."""
        # 1. contains(@class, ...) protects against trailing spaces like "inventory_item_name "
        # 2. normalize-space() strips out accidental tabs, newlines, or spaces around the product name
        xpath = (
            f"//div[contains(@class, 'inventory_item')]"
            f"[.//div[contains(@class, 'inventory_item_name') and normalize-space()='{product_name}']]"
            f"//button"
        )
        return (By.XPATH, xpath)

    def click_add_to_cart(self, product_name):
        """Clicks the 'Add to Cart' button for a specific product directly."""
        button_locator = self._get_product_button_locator(product_name)
        self.click_element(button_locator)

    def click_remove_from_cart(self, product_name):
        """Clicks the 'Remove' button for a specific product directly."""
        button_locator = self._get_product_button_locator(product_name)
        self.click_element(button_locator)
    
    def get_cart_count(self):
        """Retrieves the current count of items. Safe from 10-second TimeoutExceptions."""
        # By passing by-passing self.get_element(), we prevent the 10-second explicit wait freeze.
        # find_elements returns a list immediately (empty list if element is missing).
        badges = self.driver.find_elements(*self.SHOPPING_CART_BADGE)
        
        if len(badges) > 0:
            return int(badges[0].text)
        else:
            return 0  # Cart badge is missing from DOM, meaning count is 0