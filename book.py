from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import time

# ✅ Auto-install correct ChromeDriver
chromedriver_autoinstaller.install()

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# Launch browser
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 20)

# ---------------------------
# Step 1: Login
# ---------------------------
driver.get("https://www.facebook.com")
time.sleep(3)  # wait for page load

driver.find_element(By.ID, "email").send_keys("vidyasr90@gmail.com")
driver.find_element(By.ID, "pass").send_keys("yuvaraj6")
driver.find_element(By.NAME, "login").click()
time.sleep(5)

# ---------------------------
# Step 2: Open "Create Post" box
# ---------------------------
# Wait until "Create Post" is clickable
create_post = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='What's on your mind?']"))
)
create_post.click()
time.sleep(3)

# ---------------------------
# Step 3: Type your post
# ---------------------------
post_box = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[@role='textbox' and @contenteditable='true']"))
)
post_box.click()
post_box.send_keys("Hello! This is an automated post from Selenium.")  # your post text

time.sleep(1)

# ---------------------------
# Step 4: Click "Post" button
# ---------------------------
post_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Post']"))
)
post_button.click()

print("✅ Post submitted successfully!")

# ---------------------------
# Step 5: Wait and quit
# ---------------------------
time.sleep(5)
driver.quit()
