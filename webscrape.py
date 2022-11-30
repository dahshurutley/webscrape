from bs4 import BeautifulSoup
import requests 
import time

# css-at9mc1
r = requests.get('https://docs.github.com/en')
soup = BeautifulSoup(r.text, 'lxml')

def get_page_title(): 
    for i in soup.find_all(class_='ws-normal'):
        for x in i.find_all('h2'): 
            print(x.text) 

def get_page_title_child(): 
    for i in soup.find_all(class_='')
    

