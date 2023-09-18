from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3712125896&distance=25&f_AL=true&geoId=102713980&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

signin = driver.find_element(By.LINK_TEXT, value="Sign in")
signin.click()


username = driver.find_element(By.ID, value="username")
username.send_keys("")

password = driver.find_element(By.ID, value="password")
password.send_keys("")

sign_in = driver.find_element(By.CLASS_NAME, value="btn__primary--large")
sign_in.click()

time.sleep(30)


job_container = driver.find_elements(By.CSS_SELECTOR, value=".scaffold-layout__list-container li")
for i in job_container:
    try:
        i.click()
        save = driver.find_element(By.CSS_SELECTOR, value=".jobs-save-button span")
        save.click()
        follow = driver.find_element(By.CSS_SELECTOR, value=".artdeco-button__icon span")
        follow.click()
    except NoSuchElementException:
        pass

driver.quit()
