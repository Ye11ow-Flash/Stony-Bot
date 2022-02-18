import requests
from bs4 import BeautifulSoup
import sys
import collections

major = "cse"

def get_all_data(major):
  url = "https://www.stonybrook.edu/sb/bulletin/current/courses/"+major+"/"
  source_code = requests.get(url)
  plain_text=source_code.text
  soup = BeautifulSoup(plain_text, features="html.parser")
  data = []
  for link in soup.findAll('div',{'class' : 'course'}):
    course_data = collections.defaultdict(str)
    sbc = " "
    title = link.find('h3').text
    description = link.find('p').text
    prerequisite = link.findAll('p')[1].text
    if link.findAll('p')[2].text != "" or link.findAll('p')[2].text != "" or link.findAll('p')[2].text != " ":
      sbc = link.findAll('p')[2].text
    cred = link.findAll('p')[3].text
    course_data["title"] = title
    course_data["description"] = description
    course_data["prerequisite"] = prerequisite
    course_data["sbc"] = sbc
    course_data["cred"] = cred
    course_data["code"] = course_data["title"][4:7]
    data.append(course_data)
  return data
  
def get_course_data(course, code):
    for item in get_all_data(course):
      if item['code'] == code:
        return item