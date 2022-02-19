import requests
from bs4 import BeautifulSoup
import sys
import collections

url = "https://www.stonybrook.edu/sb/bulletin/current/courses/browse/byname/"
def get_majors_list(url):
  source_code = requests.get(url)
  plain_text=source_code.text
  soup = BeautifulSoup(plain_text, features="html.parser")
  data = []
  for link in soup.findAll("tr"):
    course_data = collections.defaultdict(str)
    major_name = link.findAll('td')[0].text
    major_code = link.findAll('td')[1].text
    course_data["major_name"] = major_name.strip(' \n\t')
    course_data["major_code"] = major_code.strip(' \n\t')[1:-1]
    data.append(course_data)
#   for i in data:
#     print(i)

get_courses(url)
