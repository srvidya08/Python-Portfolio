#Password: Vellore@6
#skyworkrajraj@gmail.com
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import  time

driver = chromedriver_autoinstaller.install()
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys('skyworkrajraj@gmail.com')
password= driver.find_element(By.XPATH,'//*[@id="pass"]')
password.send_keys(' Vellore@6')

elem = driver.find_element(By.NAME,"login")
elem.click()
statuselement= driver.find_element(By.XPATH,"//*[@name='xhpc_message']")
statuselement.click()
time.sleep(5)
buttons = driver.find_element(By.NAME,"button")
time.sleep(5)
for button in buttons:
    if button.text =='POST':
        button.click()