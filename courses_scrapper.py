import requests
from bs4 import BeautifulSoup
import sys
import collections

major = "bio"
url = "https://www.stonybrook.edu/sb/bulletin/current/courses/"+major+"/"
def get_courses(url):
  source_code = requests.get(url)
  plain_text=source_code.text
  soup = BeautifulSoup(plain_text, features="html.parser")
  data = []
  for link in soup.findAll('div',{'class' : 'course'}):
    course_data = collections.defaultdict(str)
    title = link.find('h3').text
    course_data["title"] = title.split(":")[1]
    data.append(course_data)
  # for i in data:
  #   print(i)

get_courses(url)
