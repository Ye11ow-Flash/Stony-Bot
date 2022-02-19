from webbrowser import get
import requests
from bs4 import BeautifulSoup
import sys
import collections

major = "bio"
def get_courses(major):
  url = "https://www.stonybrook.edu/sb/bulletin/current/courses/"+major+"/"
  source_code = requests.get(url)
  plain_text=source_code.text
  soup = BeautifulSoup(plain_text, features="html.parser")
  data = []
  for link in soup.findAll('div',{'class' : 'course'}):
    #course_data = collections.defaultdict(str)
    title = link.find('h3').text
    #course_data["title"] = 
    data.append(title.split(":")[1])
  # for i in data:
  #   print(i)
  return data

print(get_courses(major))

