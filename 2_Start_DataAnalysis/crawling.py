from selenium import webdriver
from bs4 import BeautifulSoup

# chromdriver 다운로드 해야함
driver = webdriver.Chrome('D:/DataAnalysis/chromedriver.exe')

url = 'http://www.melon.com/chart/index.htm'
driver.get(url)

html = driver.page_source # html을 가져오므로 웹 페이지에 접속하지 않은 상태로 데이터 처리
soup = BeautifulSoup(html, 'html.parser')

songs = soup.select('#lst50')

titlesAndSingers = [(song.select('div.ellipsis.rank01 a')[0].text, song.select('div.ellipsis.rank02 a')[0].text) for song in songs]
print(titlesAndSingers)

index = 1
for titleAndSinger in titlesAndSingers:
    print(index, titleAndSinger[0], titleAndSinger[1], sep = ' | ')
    index += 1

# 웹페이지에 접속한 상태로 데이터 처리 (연결 유지 필요하지만 페이지 조작(클릭, 입력) 가능)
songs2 = driver.find_elements_by_css_selector('#lst50')
titlesAndSingers = [(song.find_elements_by_css_selector('div.ellipsis.rank01 a')[0].text, song.find_elements_by_css_selector('div.ellipsis.rank02 a')[0].text) for song in songs2]
print(titlesAndSingers)

index = 1
for titleAndSinger in titlesAndSingers:
    print(index, titleAndSinger[0], titleAndSinger[1], sep = ' | ')
    index += 1

# html = '''
# <html>
#     <head>
#     </head>
#     <body>
#         <h1> 우리동네시장</h1>
#             <div class = 'sale'>
#                 <p id='fruits1' class='fruits'>
#                     <span class = 'name'> 바나나 </span>
#                     <span class = 'price'> 3000원 </span>
#                     <span class = 'inventory'> 500개 </span>
#                     <span class = 'store'> 가나다상회 </span>
#                     <a href = 'http://bit.ly/forPlaywithData' > 홈페이지 </a>
#                 </p>
#             </div>
#             <div class = 'prepare'>
#                 <p id='fruits2' class='fruits'>
#                     <span class ='name'> 파인애플 </span>
#                 </p>
#             </div>
#     </body>
# </html>
# '''

# from bs4 import BeautifulSoup

# soup = BeautifulSoup(html, 'html.parser')

# tags_span = soup.select('span')
# tags_p = soup.select('p')

# ids_fruits1 = soup.select('#fruits1')
# class_price = soup.select('.price')
# tags_span_class_price = soup.select('span.price')

# tags_name = soup.select('span.name')
# print(tags_name)

# tags_banana1 = soup.select('#fruits1 > span.name')
# print(tags_banana1)

