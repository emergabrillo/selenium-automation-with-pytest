import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com"  # Base URL and login page

@pytest.fixture(scope="function")
def driver():
    options = Options()
    # Uncomment the following line to enable headless mode for the browser
    # options.add_argument("--headless")
    options.add_argument("window-size=1920,1080") 

    # Built-in Selenium Manager will fetch matching driver binaries
    driver = webdriver.Chrome(options=options) 
    yield driver
    driver.quit() # Ensure the browser is closed after each test

@pytest.fixture(scope="function")
def login_page(driver, base_url):
    # Automatically loads the base URL and returns the initialized Page Object.
    driver.get(base_url)
    return LoginPage(driver)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()
    
    # Check if the test failed during the call phase
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") # Get driver from fixture
        if driver:
            try:
                # Capture screenshot as base64 NOW
                screenshot = driver.get_screenshot_as_base64()
                
                report.extras.append(pytest_html.extras.image(screenshot, mime_type="image/png"))
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")

