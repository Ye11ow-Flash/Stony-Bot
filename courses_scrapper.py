import requests
from bs4 import BeautifulSoup
import sys
import collections

def get_courses(major):
  url = "https://www.stonybrook.edu/sb/bulletin/current/courses/"+major+"/"
  source_code = requests.get(url)
  plain_text=source_code.text
  soup = BeautifulSoup(plain_text, features="html.parser")
  data = []
  for link in soup.findAll('div',{'class' : 'course'}):
    course_data = collections.defaultdict(str)
    title = link.find('h3').text
    course_data["code"] = title.split(":")[0].split("\xa0")[1]
    course_data["title"] = title.split(":")[1]
    data.append(course_data)
  # for i in data:
  #   print(i)
  return data
