import selenium
from urllib.request import urlopen

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin

##### Web scrapper for infinite scrolling page #####
driver = webdriver.Chrome(executable_path=r"/usr/local/Caskroom/chromedriver/96.0.4664.45/chromedriver")
driver.get("https://artsandculture.google.com/entity/surrealism/m073_6?categoryId=art-movement")
# driver.get("https://artsandculture.google.com/search/asset/?p=van-gogh-museum&em=m015xrq&categoryId=art-movement")
time.sleep(2)  # Allow 2 seconds for the web page to open
scroll_pause_time = 1.5 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break 

##### Extract Reddit URLs #####
urls = []
soup = BeautifulSoup(driver.page_source, "html.parser")
for a_tag in soup.findAll("a", class_="PJLMUc"):
    # import pdb; pdb.set_trace()
    link = a_tag.attrs['style']
    # extract url from link
    url = link.split('"')[1]
    print(url)
    urls.append(url)

for url in urls:
    # download image to 
    with urlopen(url) as f:
        with open("./images/{}.webp".format(url.split('/')[-1]), 'wb') as h:
            h.write(f.read())

