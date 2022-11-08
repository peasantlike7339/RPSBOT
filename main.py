import csv
import pathlib
import sys
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


CHROME_PATH = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
CHROMEDRIVER_PATH = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
WINDOW_SIZE = "1920,1080"
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
driver.maximize_window()
driver.get("https://www.rpsgame.org/random")

state= []

def writeStateToCSV(state):
    with open('data.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(state)
        f.close()

try:
    while True:
        time.sleep(5)
        if (driver.find_elements(By.CLASS_NAME, "play-page-gamer__prompt")):
            if ("Take" in driver.find_elements(By.CLASS_NAME, "play-page-gamer__prompt")[0].text):
                options = driver.find_elements(By.CLASS_NAME, "play-page-gamer__choice")
                rock = options[0]; paper = options[1]; scissors = options[2]
                if (driver.find_elements(By.CLASS_NAME, "play-page-gamer__choice")):
                    pick = random.choice(options)
                    pick.click()
                    pick = pathlib.PurePath(str(pick.get_attribute("src"))).name.replace(".svg","")
                    opponentPick = ""
                    roundResult = ""
                    while len(opponentPick)<2:
                        time.sleep(0.2)
                        opponentPick = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"play-page-gamer__choice")))
                    opponentPick = pathlib.PurePath(str(opponentPick[1].get_attribute("src"))).name.replace(".svg", "")
                    while roundResult == "":
                        roundResult = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "play-page-round-result")))
                    roundResult = roundResult.find_element(By.TAG_NAME, "span").text.strip("!YOU ")
                    state.append(pick)
                    state.append(opponentPick)
                    state.append(roundResult)
#                       print(state)
#                    writeStateToCSV(state)

        if (driver.find_elements(By.XPATH,"/html/body/app-root/app-room-page/div[@class='gradient-container gradient-container--full-height']/div[@class='container container--height-adaptive']/app-playing/section[@class='play-page-final-screen']/div[@class='play-page-final-screen__container']/section[@class='play-page-final-screen__nav']/div[@class='play-page-final-screen__nav-buttons'][1]/button[@class='btn-primary']")):
            finalResult = driver.find_element(By.CLASS_NAME, "play-page-final-screen__text").text.strip("!...").split()[1].upper()
            while (len(state) <60):
                state.append("")
            state.append(finalResult)
            print(state)
            writeStateToCSV(state)
            state =[]
            driver.find_element(By.XPATH,"/html/body/app-root/app-room-page/div[@class='gradient-container gradient-container--full-height']/div[@class='container container--height-adaptive']/app-playing/section[@class='play-page-final-screen']/div[@class='play-page-final-screen__container']/section[@class='play-page-final-screen__nav']/div[@class='play-page-final-screen__nav-buttons'][1]/button[@class='btn-primary']").click()
except Exception as e:
    trace_back = sys.exc_info()[2]
    line = trace_back.tb_lineno
    print(line)
    print(e)
    driver.quit()

driver.quit()