from selenium import webdriver
from selenium.webdriver.common.by import By
import time

timeout = time.time() + 5
five_min = time.time() + 60*5

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, value = "cookie")

store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in store]



while True:
    cookie.click()
    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        prices = [int(i.text.split("-")[1].replace(',', '').strip()) for i in all_prices if i.text !=""]
        money = int(driver.find_element(By.ID, value="money").text.replace(',', ''))
        number = 0
        number = max([i for i in prices if i < money])
        if number in prices and number<money:
            driver.find_element(By.ID, value=f"{item_ids[prices.index(number)]}").click()
                
        timeout = time.time() + 5
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID,value="cps").text
        print(cookie_per_s)
        break
driver.quit()
