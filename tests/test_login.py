def test_successful_login(login_page):
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()  
    
    # Verify successful login by checking for URL change
    assert "inventory.html" in login_page.driver.current_url

def test_incorrect_username(login_page):
    login_page.enter_username("wrong_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    
    # Verify incorrect username by checking for an error message
    error_warning = login_page.get_error_message()
    assert error_warning is not None
    # Validates the specific error message for incorrect username
    assert "Username and password do not match any user in this service" in error_warning  

def test_incorrect_password(login_page):
    login_page.enter_username("standard_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()
    
    # Verify incorrect login by checking for an error message
    error_warning = login_page.get_error_message()
    assert error_warning is not None
     # Validates the specific error message for incorrect password
    assert "Username and password do not match any user in this service" in error_warning 