from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Locators for the inventory page elements
    PRODUCT_CARDS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.CLASS_NAME, "btn_inventory")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def get_product_card_by_name(self, product_name):
        """Finds a product card by its name."""
        product_cards = self.driver.find_elements(*self.PRODUCT_CARDS)
        for card in product_cards:
            name_element = card.find_element(By.CLASS_NAME, "inventory_item_name")
            if name_element.text == product_name:
                return card
        return None  # Returns None if the product is not found

    def click_add_to_cart(self, product_name):
        """Clicks the 'Add to Cart' button for a specific product."""
        product_card = self.get_product_card_by_name(product_name)
        if product_card:
            add_to_cart_button = product_card.find_element(*self.ADD_TO_CART_BUTTONS)
            add_to_cart_button.click()

    def get_cart_count(self):
        """Retrieves the current count of items in the shopping cart."""
        try:
            cart_badge = self.get_element(self.SHOPPING_CART_BADGE)
            return int(cart_badge.text)  # Returns the count as an integer
        except:
            return 0  # Returns 0 if the cart is empty or the badge is not found

    def click_remove_from_cart(self, product_name):
        """Clicks the 'Remove' button for a specific product in the cart."""
        product_card = self.get_product_card_by_name(product_name)
        if product_card:
            remove_button = product_card.find_element(*self.ADD_TO_CART_BUTTONS)  # Assuming the same button toggles between 'Add to Cart' and 'Remove'
            remove_button.click()