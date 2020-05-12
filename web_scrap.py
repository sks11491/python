import requests
from bs4 import BeautifulSoup

page = requests.get('https://learning.codingninjas.com/competitive-programming-course/?utm_source=Google&utm_medium=cpc&utm_campaign=CN_Python_Search_Exact&utm_term=%7Bkeyword%7D&utm_source=google&utm_medium=[search]&utm_campaign=9965416469_103620826467_e_python%20full%20course__433793674724_c&gclid=EAIaIQobChMI1eumutCr6QIVjDgrCh1bkATZEAAYAiAAEgK1XvD_BwE')
soup = BeautifulSoup(page.content, 'html.parser')
container = soup.find(attrs={"data-id":'069bd38'})
element_rows = container.find_all(class_='elementor-inner-section')
image_urls = []

for elementRow in element_rows:
    image_containers = elementRow.find_all(class_='elementor-image')
    image_urls += [item.img['data-src'] for item in image_containers]
print(image_urls)
print(len(image_urls))