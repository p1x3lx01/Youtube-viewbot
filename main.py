import os
import subprocess
import itertools
import json
import random
import time
from selenium import webdriver
import undetected_chromedriver as uc
from fake_useragent import UserAgent
from colorama import Fore

def install_chrome():
    try:
        print("بدء تحميل Google Chrome...")
        subprocess.check_call(["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"])
        print("تثبيت Google Chrome...")
        subprocess.check_call(["sudo", "dpkg", "-i", "google-chrome-stable_current_amd64.deb"])
        print("تم تثبيت Google Chrome بنجاح.")
    except subprocess.CalledProcessError as e:
        print(f"حدث خطأ أثناء تثبيت Google Chrome: {e}")

def check_chrome_installed():
    try:
        subprocess.check_output(["/usr/bin/google-chrome-stable", "--version"], stderr=subprocess.STDOUT)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


class Viewbot:
    def __init__(self):
        self.config = json.load(open('./data/config.json', 'r+'))
        self.proxies = itertools.cycle(open('./data/proxies.txt').read().splitlines())
        self.ua = UserAgent()

    def ui(self):
        os.system('cls && title Youtube Viewbot ^| github.com/Plasmonix' if os.name == "nt" else 'clear') 
        print(f"""{Fore.RED}                                                           
         __ __         _       _          _____ _           _       _     
        |  |  |___ _ _| |_ _ _| |_ ___   |  |  |_|___ _ _ _| |_ ___| |_   
        |_   _| . | | |  _| | | . | -_|  |  |  | | -_| | | | . | . |  _|  
          |_| |___|___|_| |___|___|___|   \___/|_|___|_____|___|___|_|    
        {Fore.RESET}""")

    def open_url(self, ua, sleep_time, proxy):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--incognito")
        self.options.add_argument('--start-maximized')
        self.options.add_argument('user-agent=%s' % ua.random)
        self.options.add_argument("--proxy-server=%s" % proxy)
        self.options.headless = True

        self.browser = uc.Chrome(options=self.options)
        self.browser.get(self.config["url"])
        time.sleep(sleep_time)
        self.browser.quit()

    def main(self):
        self.ui()
        for _ in range(self.config["views"]):
            sleeptime = random.randint(self.config["min_watch"], self.config["max_watch"])
            self.open_url(self.ua, sleeptime, next(self.proxies))

if __name__ == "__main__":
    if not check_chrome_installed():
        print("Google Chrome غير مثبت. يتم الآن تثبيته...")
        install_chrome()
    else:
        print("Google Chrome مثبت بالفعل.")

    bot = Viewbot()
    bot.main()
