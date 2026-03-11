#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""检查所有参数是否都被提取"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import requests
import re

# 获取搜索页面
html = requests.get('https://www.fhysc.com/user/search.html?q=test', timeout=15).text

# 定义所有必需的参数名
required_params = ['vw', 'abw', 'ru', 'jrt', 'van', 'fw', 'cwl', 'gpr', 'uyoo', 'tz',
                  'euu', 'tsn', 'eju', 'um', 'fp', 'dvm', 'jpk', 'deblkx', 'ht',
                  'azy', 'sna', 'wqx', 'fpp', 'rup', 'jwj', 'bgt', 'qp', 'yf', 'cw', 'wq', 'sign']

print("必需的参数:")
print(required_params)
print(f"总数: {len(required_params)}")

# 使用正则提取所有参数
pattern = r'var (vw|abw|ru|jrt|van|fw|cwl|gpr|uyoo|tz|euu|tsn|eju|um|fp|dvm|jpk|deblkx|ht|azy|sna|wqx|fpp|rup|jwj|bgt|qp|yf|cw|wq|sign)="([^"]+)"'
matches = re.findall(pattern, html)

print(f"\n实际提取到的参数:")
extracted_params = [m[0] for m in matches]
print(extracted_params)
print(f"总数: {len(extracted_params)}")

# 检查缺失的参数
missing = set(required_params) - set(extracted_params)
print(f"\n缺失的参数: {missing}")

# 检查 HTML 中的实际写法
print("\n检查 HTML 中缺失参数的写法:")
for param in missing:
    # 搜索该参数在 HTML 中的定义
    for line in html.split('\n'):
        if f'var {param}' in line:
            print(f"{param}: {line.strip()}")
