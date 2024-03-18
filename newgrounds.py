from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from urllib.request import Request, urlopen
import urllib.request
import os

image_links = []
post_links = []
user_input = input('Enter Link: ')

options = Options()

# Reset Cache
options.add_argument('--disk-cache-size=0')

# EDIT BASED ON USER CONFIG
options.add_argument("--user-data-dir=/home/dokorege/.config/google-chrome/ ")
options.add_argument("--mute-audio")

# EDIT BASED ON BINARY OF CHROME PROFILE
options.binary_location = ""


driver = webdriver.Chrome(chrome_options = options, executable_path='/home/dokorege/Downloads/chromedriver')
driver.get(user_input)
time.sleep(2)
soup = BeautifulSoup(driver.page_source, 'lxml')

for i in soup.find_all(class_='user-link'):
    test = ''.join(i.text.strip())
    print(test)
    



try:
    # EDIT CREATION OF DIRECTORY
    os.makedirs(f"")
except FileExistsError:
    # directory already exists
    pass

def posts():
    soup = BeautifulSoup(driver.page_source, 'lxml')
    for i in soup.find_all(class_='current'):
        print(int(i.find('strong').text))
        return int(i.find('strong').text)

nums = posts()


def paginator():
    num = round(nums / 3) 
    
    if nums >= 30: 
        for i in range(0,num):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'lxml')

    for i in soup.find_all(class_='inline-card-portalsubmission'):
        post_links.append(i['href'])
    print(len(post_links))




def download():
    counter = 0 
    for i in post_links:
        driver.get(i)
        if BeautifulSoup(driver.page_source, 'lxml').find(class_='play-wrapper-inner'):
            driver.find_element(By.CLASS_NAME, 'play-wrapper-inner').click()
        else:
            print('Game')
            continue

        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'lxml')

        if soup.find('source'):
            for i in soup.find_all('source'):
                print(i['src'])
                urllib.request.urlretrieve(i['src'], f"{counter}.mp4")
                counter += 1
        else:
            print('Game Detected.')
 

paginator()
download()
