from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyfiglet

banner = pyfiglet.figlet_format('Spoof Browser')
print(banner)

options = Options()
options.headless = False
options.add_experimental_option("detach", True)
#options.add_argument("--window-size=1920,1200")
link = input("URL you would like to open: ")
print('\n')
num = int(input("How many browsers would you like to open: "))

def openBrowser(link, num):
    driver = webdriver.Chrome(options=options, executable_path='../chromedriver')
    driver.get(link)

for i in range(num):
    i = webdriver.Chrome(options=options, executable_path='../chromedriver')
    i.get(link)