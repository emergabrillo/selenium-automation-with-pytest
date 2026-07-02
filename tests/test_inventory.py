from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_add_and_remove_product_from_inventory_page(driver, base_url):
    driver.get(base_url)
    
    # Perform login first
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Now on the inventory page, add a product to the cart
    inventory_page = InventoryPage(driver)
    product_name = "Sauce Labs Backpack"  # Example product name
    inventory_page.click_add_to_cart(product_name)
    # Verify that the product was added to the cart
    cart_count = inventory_page.get_cart_count()
    assert cart_count == 1  # Checks if the cart count is updated to 1 after adding a product
    # Verify that the product can be removed through the inventory page
    inventory_page.click_remove_from_cart(product_name)
    cart_count = inventory_page.get_cart_count()
    assert cart_count == 0  # Checks if the cart count is updated to 0 after removing the product