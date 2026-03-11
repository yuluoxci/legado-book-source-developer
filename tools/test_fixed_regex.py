#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""测试修正后的正则表达式"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import requests
import re

html = requests.get('https://www.fhysc.com/user/search.html?q=test', timeout=15).text

# 新的正则表达式：允许等号前后有空格
pattern = r'var\s+(vw|abw|ru|jrt|van|fw|cwl|gpr|uyoo|tz|euu|tsn|eju|um|fp|dvm|jpk|deblkx|ht|azy|sna|wqx|fpp|rup|jwj|bgt|qp|yf|cw|wq|sign)\s*=\s*"([^"]+)"'
matches = re.findall(pattern, html)

print(f"提取到的参数数量: {len(matches)}")
print(f"提取到的参数: {[m[0] for m in matches]}")

# 模拟 JavaScript 的 map 处理
params_list = []
for param_name, param_value in matches:
    # 模拟: arr=m.split('"'); return arr[0].replace(/var\s+/, '')+'='+arr[1];
    # 假设 m = 'var ru  = "193a426x"'
    parts = html.split(f'{param_name}')[0].split('var ')
    # 更简单的方法：直接构造
    params_list.append(f"{param_name}={param_value}")

params = '&'.join(params_list)
print(f"\n生成的参数:")
print(params[:200] + "...")
