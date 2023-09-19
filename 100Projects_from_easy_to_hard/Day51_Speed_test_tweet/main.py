from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach',True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://www.speedtest.net")
        self.up = 0
        self.down = 0
    
    def get_internet_speed(self):
        self.speed = self.driver.find_element(By.CLASS_NAME, value="start-text")
        self.speed.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, value="download-speed")
        self.up = self.driver.find_element(By.CLASS_NAME, value="upload-speed")
        print(self.down.text)
        print(self.up.text)
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        email.send_keys("TWITTER_EMAIL")
        password.send_keys("TWITTER_PASSWORD")
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {300}down/{100}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()

tweet = InternetSpeedTwitterBot()
tweet.get_internet_speed()
tweet.tweet_at_provider()