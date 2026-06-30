import time, pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
POST_TEXT = "Hi this is selenium!"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/"); time.sleep(2)
for c in pickle.load(open("fb_cookies.pkl","rb")): c.pop("sameSite", None); driver.add_cookie(c)
driver.refresh(); time.sleep(4)
wait = WebDriverWait(driver, 20)
textbox = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox' and @contenteditable='true']")))
driver.execute_script("arguments[0].scrollIntoView(); arguments[0].focus();", textbox)
for ch in POST_TEXT: textbox.send_keys(ch); time.sleep(0.05)
post_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Post' or contains(text(),'Post')]")))
post_btn.click()

time.sleep(3)
driver.quit()
print("Done")
