import sys
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_PATH = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
CHROMEDRIVER_PATH = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
WINDOW_SIZE = "1920,1080"
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
driver.maximize_window()
driver.get("https://www.rpsgame.org")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/app-root/app-homepage/div[@class='gradient-container']/div[@class='container container--height-adaptive']/section[@class='homepage-nav']/div[@class='homepage-nav__buttons']/button[@class='btn-secondary homepage-nav__btn-secondary']").click()

gameCount = 0;
try:
    while (gameCount <3):
        time.sleep(5)
        if (driver.find_elements(By.CLASS_NAME, "play-page-gamer__prompt")):
            if ("Take" in driver.find_elements(By.CLASS_NAME, "play-page-gamer__prompt")[0].text):
                options = driver.find_elements(By.CLASS_NAME, "play-page-gamer__choice")
                rock = options[0]; paper = options[1]; scissors = options[2]
                if (driver.find_elements(By.CLASS_NAME, "play-page-gamer__choice")):
                    random.choice(options).click()
        if (driver.find_elements(By.XPATH,"/html/body/app-root/app-room-page/div[@class='gradient-container gradient-container--full-height']/div[@class='container container--height-adaptive']/app-playing/section[@class='play-page-final-screen']/div[@class='play-page-final-screen__container']/section[@class='play-page-final-screen__nav']/div[@class='play-page-final-screen__nav-buttons'][1]/button[@class='btn-primary']")):
            driver.find_element(By.XPATH,"/html/body/app-root/app-room-page/div[@class='gradient-container gradient-container--full-height']/div[@class='container container--height-adaptive']/app-playing/section[@class='play-page-final-screen']/div[@class='play-page-final-screen__container']/section[@class='play-page-final-screen__nav']/div[@class='play-page-final-screen__nav-buttons'][1]/button[@class='btn-primary']").click()
            gameCount = gameCount + 1
except Exception as e:
    trace_back = sys.exc_info()[2]
    line = trace_back.tb_lineno
    print(line)
    print(e)
    driver.quit()

driver.quit()