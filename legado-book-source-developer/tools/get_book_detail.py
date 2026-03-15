import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# 获取书籍详情页
book_url = 'https://www.fhysc.com/xs/54/54144/'
r = requests.get(book_url, headers=headers, timeout=15)
print(f'Status: {r.status_code}')
print(f'Encoding: {r.encoding}')

with open('fhysc_book_detail.html', 'w', encoding='utf-8') as f:
    f.write(r.text)

soup = BeautifulSoup(r.text, 'html.parser')

# 查找标题
h1 = soup.find('h1')
print(f'\nBook Title: {h1.text if h1 else "N/A"}')

# 查找详情信息
info = soup.find('div', class_='info')
if info:
    print('\nInfo Section:')
    print(info.prettify()[:500])

# 查找目录
catalog = soup.find('div', id='catalog')
if catalog:
    chapters = catalog.find_all('a')
    print(f'\nChapters: {len(chapters)}')
    if chapters:
        print(f'First chapter: {chapters[0].text} -> {chapters[0].get("href")}')
        print(f'Last chapter: {chapters[-1].text} -> {chapters[-1].get("href")}')
        
        # 获取第一章内容
        first_chapter_url = 'https://www.fhysc.com' + chapters[0].get('href')
        r2 = requests.get(first_chapter_url, headers=headers, timeout=15)
        with open('fhysc_chapter_content.html', 'w', encoding='utf-8') as f:
            f.write(r2.text)
        print(f'\nChapter page saved: fhysc_chapter_content.html')
        
        soup2 = BeautifulSoup(r2.text, 'html.parser')
        content = soup2.find('div', id='content')
        if content:
            print(f'Content length: {len(content.text)} characters')
            print(f'Content preview: {content.text[:200]}')
