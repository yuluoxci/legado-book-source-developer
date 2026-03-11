#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""分析网站 JavaScript 参数生成逻辑"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import requests
from bs4 import BeautifulSoup
import re

print("=" * 60)
print("分析网站 JavaScript 参数")
print("=" * 60)

# 1. 获取首页，提取 JS 变量
print("\n【步骤1】获取首页 JS 变量")
print("-" * 60)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
r = requests.get('https://www.fhysc.com/', headers=headers, timeout=15)
soup = BeautifulSoup(r.text, 'html.parser')

# 查找所有 script 标签中的变量定义
scripts = soup.find_all('script')
js_vars = {}

for script in scripts:
    if script.string:
        # 匹配类似 var vw="..."; 的变量定义
        matches = re.findall(r'var\s+(\w+)\s*=\s*["\']([^"\']+)["\']', script.string)
        for var_name, var_value in matches:
            js_vars[var_name] = var_value

print(f"找到的 JS 变量 ({len(js_vars)} 个):")
for key, value in sorted(js_vars.items()):
    print(f"  {key}: {value}")

# 2. 分析关键参数
print("\n【步骤2】分析 curl 中的参数")
print("-" * 60)

curl_params = {
    'q': '校花',
    'vw': '934q624r229X547q',
    'abw': '514V686960r220w304q',
    'ru': '877Z381731z334N',
    'jrt': '827640356588214J',
    'van': '212D304K301D356i31',
    'fw': '588B60954Z659b547R',
    'cwl': '903s286628A464G425L',
    'gpr': '714P662B957B',
    'uyoo': '219Q771u7973662',
    'tz': '221Q246A657T',
    'euu': '409Z230v148v832R69r',
    'tsn': '535M261L950P504I692469Q',
    'eju': '242Q999b237M423c',
    'um': '178t',
    'fp': '392q869Q898X816I947n',
    'dvm': '260a403D275w',
    'jpk': '452877Z225',
    'deblkx': '46J610V358K739645O',
    'ht': '179V875V155m',
    'azy': '115601Y363',
    'sna': '393U178n878778I601G',
    'wqx': '255x',
    'fpp': '476W887d',
    'rup': '761n624l499m',
    'jwj': '640x519B138t364Y564Y',
    'bgt': '528y79M3',
    'qp': '858l881484744N153M',
    'yf': '587C997y254l',
    'cw': '298j676c842925A44f210m',
    'wq': '911y372O251q',
    'sign': '8d5992f756c5abfed3df6e395c1def5c'
}

print("curl 参数:")
for key in sorted(curl_params.keys()):
    value = curl_params[key]
    # 检查是否与首页 JS 变量匹配
    if key in js_vars:
        status = "✓ 匹配首页变量" if value == js_vars[key] else "✗ 与首页变量不同"
    else:
        status = "- 首页无此变量"
    print(f"  {key:15s}: {value[:50]:50s} {status}")

# 3. 获取并分析 common.js
print("\n【步骤3】获取并分析 common.js")
print("-" * 60)

try:
    r_js = requests.get('https://www.fhysc.com/js/common.js', headers=headers, timeout=15)
    print(f"common.js 大小: {len(r_js.text)} 字符")
    
    # 搜索与搜索相关的函数
    print("\n搜索相关代码:")
    lines = r_js.text.split('\n')
    for i, line in enumerate(lines, 1):
        if 'search' in line.lower() or 'sign' in line.lower():
            print(f"  Line {i}: {line.strip()[:100]}")
    
    # 保存 common.js 供后续分析
    with open('common.js', 'w', encoding='utf-8') as f:
        f.write(r_js.text)
    print("\n已保存 common.js 到文件")
except Exception as e:
    print(f"获取 common.js 失败: {e}")

# 4. 总结
print("\n【总结】")
print("-" * 60)
print("分析结论:")
print("1. 网站使用动态生成的参数作为反爬虫机制")
print("2. 参数包括:")
print("   - sign: 签名（可能是加密生成）")
print("   - vw, abw, fw 等: 浏览器指纹相关")
print("   - 多个短随机字符串: 可能与时间戳、会话相关")
print("3. 部分参数可能在首页 JavaScript 中定义")
print("4. sign 参数需要逆向 common.js 中的加密逻辑")
