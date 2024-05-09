from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure Selenium
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# URL and login credentials
url = "https://demo.dealsdray.com/"
username = "prexo.mis@dealsdray.com"
password = "prexo.mis@dealsdray.com"

# Path for the file to be uploaded
file_path = r"D:\Automation-Functional-testing\input\demo-data (1).xlsx"
screenshot_path = r"D:\Automation-Functional-testing\screeshot"

try:
    # Navigate to the panel URL
    driver.get(url)

    # Wait for the login form to load and enter credentials
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "username_input_id"))
    ).send_keys(username)

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "password_input_id"))
    ).send_keys(password)

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "login_button_id"))
    ).click()

    # Wait for the page to load after login
    time.sleep(5)  # Increase this if needed

    # Click the upload button
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "file_upload_button_id"))
    ).click()  # Open file upload dialog

    # Find the file input field and upload the XLS file
    file_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "mui-612"))
    )
    
    file_input.send_keys(file_path)  # Upload the file

    # Wait for the upload to complete
    time.sleep(10)  # Adjust based on the expected upload time

    # Take a screenshot of the final output page
    driver.save_screenshot(screenshot_path)

finally:
    # Close the browser
    driver.quit()
