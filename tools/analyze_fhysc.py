#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""获取 fhysc.com 网站信息"""

import sys
import io

# 设置输出编码为 UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("=" * 60)
print("步骤 1：检测网站编码")
print("=" * 60)

try:
    # 获取首页
    response = requests.get('https://www.fhysc.com/', timeout=15, headers=headers)
    print(f"状态码: {response.status_code}")
    print(f"响应编码: {response.encoding}")
    print(f"Content-Type: {response.headers.get('Content-Type')}")
    print(f"实际编码: {response.apparent_encoding}")
    print(f"页面长度: {len(response.text)} 字符")
    
    # 保存首页 HTML
    with open('fhysc_home.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
    print("✓ 首页 HTML 已保存到 fhysc_home.html")
except Exception as e:
    print(f"✗ 错误: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# 2. 尝试搜索
print("\n" + "=" * 60)
print("步骤 2：测试搜索接口")
print("=" * 60)

# 常见笔趣阁搜索接口格式
search_urls = [
    ('GET', 'https://www.fhysc.com/modules/article/search.php?searchkey=凡人修仙传&searchtype=all'),
    ('POST', 'https://www.fhysc.com/modules/article/search.php', {'searchkey': '凡人修仙传', 'searchtype': 'all'}),
    ('GET', 'https://www.fhysc.com/search.php?q=凡人修仙传'),
    ('GET', 'https://www.fhysc.com/search?keyword=凡人修仙传'),
]

for method, url, *args in search_urls:
    try:
        if method == 'GET':
            search_response = requests.get(url, timeout=10, headers=headers)
        else:
            search_response = requests.post(url, data=args[0], timeout=10, headers=headers)
        
        print(f"✓ 成功: {method} {url}")
        print(f"  状态码: {search_response.status_code}")
        print(f"  编码: {search_response.encoding}")
        print(f"  长度: {len(search_response.text)} 字符")
        
        # 保存搜索结果
        with open('fhysc_search.html', 'w', encoding='utf-8') as f:
            f.write(search_response.text)
        print("  ✓ 搜索结果已保存到 fhysc_search.html")
        break
    except Exception as e:
        print(f"✗ 失败: {method} {url}")
        print(f"  错误: {str(e)[:100]}")

# 3. 分析首页结构
print("\n" + "=" * 60)
print("步骤 3：分析首页结构")
print("=" * 60)
soup = BeautifulSoup(response.text, 'html.parser')

# 查找常见元素
common_elements = {
    'class="newbox"': soup.find_all('div', class_='newbox'),
    'id="catalog"': soup.find_all('div', id='catalog'),
    'class="content"': soup.find_all('div', class_='content'),
    'class="intro"': soup.find_all('div', class_='intro'),
    'class="booknav2"': soup.find_all('div', class_='booknav2'),
    'class="bookimg2"': soup.find_all('div', class_='bookimg2'),
    'class="txtnav"': soup.find_all('div', class_='txtnav'),
    'tag.h1': soup.find_all('h1'),
    'tag.img': soup.find_all('img'),
}

for selector, elements in common_elements.items():
    if elements:
        print(f"✓ 找到 {len(elements)} 个 {selector} 元素")

# 4. 查找书籍列表链接
print("\n" + "=" * 60)
print("步骤 4：查找书籍链接")
print("=" * 60)

book_links = soup.find_all('a', href=True)
print(f"找到 {len(book_links)} 个链接")

# 查找可能是书籍链接的 pattern
book_url_patterns = [
    '/book/',
    '/novel/',
    '/html/',
    '.html',
]

for pattern in book_url_patterns:
    matching_links = [a for a in book_links if pattern in a.get('href', '')]
    if matching_links:
        print(f"✓ 包含 '{pattern}' 的链接: {len(matching_links)} 个")
        if len(matching_links) <= 5:
            for link in matching_links[:3]:
                print(f"  - {link.get('href', '')}")

# 5. 获取一本书的详情页
print("\n" + "=" * 60)
print("步骤 5：获取书籍详情页")
print("=" * 60)

# 尝试找到一个书籍链接
book_link = None
for link in book_links:
    href = link.get('href', '')
    if any(p in href for p in book_url_patterns) and not href.startswith('#'):
        book_link = href
        if not book_link.startswith('http'):
            book_link = 'https://www.fhysc.com' + book_link
        print(f"选择书籍链接: {book_link}")
        break

if book_link:
    try:
        detail_response = requests.get(book_link, timeout=10, headers=headers)
        print(f"详情页状态码: {detail_response.status_code}")
        
        with open('fhysc_detail.html', 'w', encoding='utf-8') as f:
            f.write(detail_response.text)
        print("✓ 详情页已保存到 fhysc_detail.html")
        
        # 分析详情页
        detail_soup = BeautifulSoup(detail_response.text, 'html.parser')
        
        # 查找章节列表
        catalog = detail_soup.find('div', id='catalog')
        if catalog:
            chapters = catalog.find_all('a')
            print(f"✓ 找到 {len(chapters)} 个章节")
            if chapters:
                first_chapter = 'https://www.fhysc.com' + chapters[0].get('href', '')
                print(f"  第一章链接: {first_chapter}")
                
                # 获取第一章内容
                try:
                    content_response = requests.get(first_chapter, timeout=10, headers=headers)
                    with open('fhysc_content.html', 'w', encoding='utf-8') as f:
                        f.write(content_response.text)
                    print("✓ 内容页已保存到 fhysc_content.html")
                except Exception as e:
                    print(f"✗ 获取内容页失败: {e}")
        else:
            print("✗ 未找到章节列表")
            
    except Exception as e:
        print(f"✗ 获取详情页失败: {e}")
else:
    print("✗ 未找到书籍链接")

print("\n" + "=" * 60)
print("信息收集完成！")
print("=" * 60)
