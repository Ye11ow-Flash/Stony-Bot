import requests
import lxml.html


def get_degree_info(major):
    link = f"https://www.stonybrook.edu/sb/bulletin/current/academicprograms/{major}/about.php"
    html = requests.get(link)
    doc = lxml.html.fromstring(html.content)
    text = doc.xpath('//*[@id="column_2"]/div/p[1]/text()')
    return(text)
