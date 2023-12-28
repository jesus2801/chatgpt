from urllib.request import urlopen, urlretrieve
import requests

from pathlib import Path
from os.path import join
from os import makedirs
import shutil

from SpeechToText import SpeechToText

from bs4 import BeautifulSoup

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

import time


class Scrapping:
    speech = SpeechToText()
    __downloads_path = join(Path.home(), "Downloads/")

    def getPronunciation(self, text: str):
        url = "https://ssl.gstatic.com/dictionary/static/pronunciation/2022-03-02/audio/" + \
            text[0:2] + "/" + text + "_en_us_1.mp3"

        r = requests.get(url)
        if (r.status_code != 404):
            with urlopen(url) as response, open(join(self.__downloads_path, text + ".mp3"), 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
        else:
            print("not found on how to pronounce")
            self.speech.synthesize_text(text, join(
                self.__downloads_path, text + ".mp3"))

    def getWordCategories(self, word: str):
        url = "https://translate.google.com/?sl=en&tl=es&text=" + word + "&op=translate"

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options)
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'Nv4rrc')))

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        elements_soup = soup.find_all('div', {"class": "Nv4rrc"})

        l = set()

        for element in elements_soup:
            l.add(element.text)

        driver.quit()
        return list(l)

    def scrape_images(self, word: str):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(chrome_options)

        url = (
            "https://www.google.com/search?q={s}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568")

        driver.get(url.format(s=word + "+images"))

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(5)

        imgResults = driver.find_elements(
            By.XPATH, "//img[contains(@class,'Q4LuWd')]")

        src = []
        for img in imgResults:
            src.append(img.get_attribute('src'))

        path = join(self.__downloads_path, word + "/")
        makedirs(path)
        for i in range(10):
            urlretrieve(str(src[i]), join(
                self.__downloads_path, word + "/{}.jpg".format(i)))

        driver.quit()
