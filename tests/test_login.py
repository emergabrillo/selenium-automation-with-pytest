from pages.login_page import LoginPage

def test_successful_login(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    login_page = LoginPage(driver)
    login_page.enter_username("student")
    login_page.enter_password("Password123")
    login_page.click_login()  
    
    # Verify successful login by checking for a specific element or URL change
    assert "Logged In Successfully" in driver.page_source  # Checks if the success message is present in the page source after login

def test_incorrect_username(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    login_page = LoginPage(driver)
    login_page.enter_username("wrong_user")
    login_page.enter_password("Password123")
    login_page.click_login()
    
    # Verify incorrect username by checking for an error message
    error_warning = login_page.get_error_message()
    assert error_warning is not None  # Checks if an error message is displayed
    assert error_warning == "Your username is invalid!"  # Validates the specific error message for incorrect username

def test_incorrect_password(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    login_page = LoginPage(driver)
    login_page.enter_username("student")
    login_page.enter_password("password321")
    login_page.click_login()
    
    # Verify incorrect login by checking for an error message
    error_warning = login_page.get_error_message()
    assert error_warning is not None  # Checks if an error message is displayed
    assert error_warning == "Your password is invalid!"  # Validates the specific error message for incorrect password