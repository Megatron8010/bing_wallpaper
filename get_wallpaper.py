import shutil
import requests
from bs4 import BeautifulSoup
from datetime import date
import os

bing_path = 'http://www.bing.com'
bing_url = 'https://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=en-US'

def date_generator():
    today = str(date.today())
    return today

def download():
    url = url_generator()
    today = date_generator()
    file_name= today + 'img.png'
    response = requests.get(url,stream = True)
    with open(file_name,'wb') as out:
        shutil.copyfileobj(response.raw,out)
    del response    

def url_generator():
    res = requests.get(bing_url)
    soup = BeautifulSoup(res.text,'lxml')  #might have to pip install lxml
    soup_url = soup.find('url').text
    url = bing_path + soup_url
    return url
    

    
    
    
