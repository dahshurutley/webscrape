from bs4 import BeautifulSoup
import requests 
import time

# css-at9mc1
r = requests.get('https://www.taehs.org/apps/bell_schedules/')
soup = BeautifulSoup(r.text, 'lxml')


def get_main_schedule(): 
    # Iterates through the bell schedule 
    for i in soup.find_all(class_='bell-schedule'):
        # Iterates through description for tables 
        for z in i.find_all('caption'):  
            # Determines if Monday is in the caption, therefore posts
            if 'Monday' in z.text: 
                # Since Monday is in the desc, only prints out the schedule for Monday Tuesday Thursday and Friday. 
                # Iterates through Table Row elements and prints their text content. 
                for x in i.find_all('tr'):
                    print(x.text)


def get_wensday_schedule(): 
    # Iterates through the bell schedule 
    for i in soup.find_all(class_='bell-schedule'):
        # Iterates through description for tables 
        for z in i.find_all('caption'):  
            # Determines if Wednesday is in the caption, therefore posts
            if 'Wednesday' in z.text: 
                # Since Wednesday is in the desc, only prints out the schedule for Wensday. 
                # Iterates through Table Row elements and prints their text content. 
                for x in i.find_all('tr'):
                    print(x.text)




get_main_schedule()
print('-----------------------------------------')
get_wensday_schedule()

