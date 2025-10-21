from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome options for Jenkins/CI
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-popup-blocking")

# Start ChromeDriver
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15)

# Open your Kubernetes app (use the correct NodePort)
driver.get("http://localhost:32196")  # <-- use the correct port shown in kubectl get svc
wait.until(EC.presence_of_element_located((By.NAME, "full_name")))
time.sleep(1)

# Fill the form
driver.find_element(By.NAME, "full_name").send_keys("Test User")
driver.find_element(By.NAME, "email").send_keys("test_user@gmail.com")
driver.find_element(By.NAME, "username").send_keys("testuser123")
driver.find_element(By.NAME, "password").send_keys("password123")
driver.find_element(By.NAME, "confirm_password").send_keys("password123")
driver.find_element(By.NAME, "phone").send_keys("9876543210")
driver.find_element(By.NAME, "dob").send_keys("2000-01-01")
driver.find_element(By.NAME, "gender").send_keys("Male")
driver.find_element(By.NAME, "address").send_keys("Hyderabad, India")

# Scroll to submit button and click
submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()

# Wait for confirmation (optional)
time.sleep(3)
print("Test Completed Successfully!")
driver.quit()
