from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Number of times to run the test
RUN_COUNT = 5

for i in range(RUN_COUNT):
    print(f"\nRunning Test #{i+1}...")

    driver = webdriver.Chrome()
    driver.get("http://localhost:32196")  # Use correct NodePort
    time.sleep(2)

    # Fill the form (with unique data each time)
    driver.find_element(By.NAME, "full_name").send_keys(f"Test User {i+1}")
    driver.find_element(By.NAME, "email").send_keys(f"test_user{i+1}@gmail.com")
    driver.find_element(By.NAME, "username").send_keys(f"user{i+1}")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.NAME, "confirm_password").send_keys("password123")
    driver.find_element(By.NAME, "phone").send_keys(f"98765432{i+1:02d}")
    driver.find_element(By.NAME, "dob").send_keys("2000-01-01")
    driver.find_element(By.NAME, "gender").send_keys("Male")
    driver.find_element(By.NAME, "address").send_keys("Hyderabad, India")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)

    print(f"Test #{i+1} Completed Successfully!")
    driver.quit()
    time.sleep(2)  # wait before next iteration



