import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# 获取第一章内容
chapter_url = 'https://www.fhysc.com/xs/54/54144/31791010.html'
r = requests.get(chapter_url, headers=headers, timeout=15)
print(f'Status: {r.status_code}')
print(f'Encoding: {r.encoding}')

with open('fhysc_chapter_content.html', 'w', encoding='utf-8') as f:
    f.write(r.text)

soup = BeautifulSoup(r.text, 'html.parser')

# 查找内容
content = soup.find('div', id='content')
if content:
    print(f'\nContent length: {len(content.text)} characters')
    print(f'\nContent preview:\n{content.text[:500]}')
else:
    print('\nContent not found!')
    # 查找其他可能的容器
    for div in soup.find_all('div'):
        if 'class' in div.attrs and any('content' in c.lower() for c in div.attrs['class']):
            print(f"Found: {div.attrs['class']}")
