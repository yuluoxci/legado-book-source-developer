#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
直链上传工具 - Legado Book Source Developer

功能：
1. 将书源内容上传到图床/云存储
2. 返回可访问的直链
3. 支持多种上传方式配置
4. 美化返回结果
"""

import json
import requests
import os
import sys
from pathlib import Path
from typing import Dict, Any, Optional, Tuple
from datetime import datetime

# 设置Windows控制台输出编码
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


class BookSourceUploader:
    """书源直链上传器"""

    def __init__(self):
        self.references_dir = Path(__file__).parent.parent / 'references'

    def upload_book_source(
        self,
        book_source_json: Dict[str, Any],
        upload_config: Optional[Dict[str, Any]] = None
    ) -> Tuple[bool, Dict[str, Any]]:
        """
        上传书源内容到图床

        Args:
            book_source_json: 书源JSON对象
            upload_config: 上传配置（如果为None则使用默认配置）

        Returns:
            (success, result): 成功标志和结果字典
        """
        # 默认上传配置
        if upload_config is None:
            upload_config = {
                "compress": False,
                "downloadUrlRule": "$.data.links.url",
                "summary": "鲸落图床",
                "uploadUrl": "https://tu.406np.xyz/api/v1/upload",
                "method": "POST",
                "headers": {"Accept": "application/json"},
                "body": {"file": "fileRequest", "show": "1"},
                "type": "multipart/form-data"
            }

        try:
            # 提取上传配置
            upload_url = upload_config.get('uploadUrl', '')
            method = upload_config.get('method', 'POST').upper()
            headers = upload_config.get('headers', {})
            body_config = upload_config.get('body', {})
            content_type = upload_config.get('type', 'multipart/form-data')
            download_rule = upload_config.get('downloadUrlRule', '$..url')

            if not upload_url:
                return False, {'error': '上传URL为空', 'details': 'uploadUrl配置缺失'}

            # 准备上传内容
            book_source_content = json.dumps(book_source_json, ensure_ascii=False, indent=2)
            book_source_name = book_source_json.get('bookSourceName', 'unknown') + '.json'

            # 构建请求参数
            files = {}
            data = {}

            for key, value in body_config.items():
                if value == 'fileRequest':
                    # 文件字段
                    files[key] = (book_source_name, book_source_content, 'application/json')
                else:
                    # 普通表单字段
                    data[key] = value

            # 发送请求
            if method == 'POST':
                if content_type == 'multipart/form-data':
                    response = requests.post(upload_url, headers=headers, files=files, data=data, timeout=30)
                else:
                    # JSON格式
                    headers['Content-Type'] = 'application/json'
                    json_body = {}
                    for key, value in body_config.items():
                        if value == 'fileRequest':
                            json_body[key] = book_source_content
                        else:
                            json_body[key] = value
                    response = requests.post(upload_url, headers=headers, json=json_body, timeout=30)
            else:
                return False, {'error': f'不支持的请求方法: {method}', 'details': '当前仅支持POST'}

            # 检查响应
            if response.status_code == 200:
                result_data = response.json()

                # 提取下载链接
                download_url = self._extract_download_url(result_data, download_rule)

                if download_url:
                    # 美化返回结果
                    formatted_result = self._format_success_result(
                        book_source_json,
                        upload_config,
                        result_data,
                        download_url
                    )
                    return True, formatted_result
                else:
                    return False, {
                        'error': '无法提取下载链接',
                        'details': f'规则: {download_rule}',
                        'response': result_data
                    }
            else:
                return False, {
                    'error': f'上传失败: HTTP {response.status_code}',
                    'details': response.text
                }

        except requests.exceptions.Timeout:
            return False, {'error': '请求超时', 'details': '上传服务响应超过30秒'}
        except requests.exceptions.ConnectionError:
            return False, {'error': '连接失败', 'details': '无法连接到上传服务器'}
        except json.JSONDecodeError:
            return False, {'error': '响应解析失败', 'details': '服务器返回的不是有效的JSON'}
        except Exception as e:
            return False, {'error': f'上传异常: {str(e)}', 'details': str(type(e).__name__)}

    def _extract_download_url(self, data: Any, rule: str) -> Optional[str]:
        """
        根据规则提取下载链接

        Args:
            data: 响应数据
            rule: 提取规则（简化版JSONPath）

        Returns:
            提取的URL，如果失败返回None
        """
        try:
            if rule == '$':
                return data
            elif rule.startswith('$..'):
                # JSONPath简化支持 - 深度查找
                key = rule[3:]
                if isinstance(data, dict):
                    return data.get(key)
                elif isinstance(data, list) and len(data) > 0:
                    if isinstance(data[0], dict):
                        return data[0].get(key)
            elif rule.startswith('$.'):
                # JSONPath点路径支持 - 如 $.data.links.url
                path = rule[2:].split('.')
                current = data
                for key in path:
                    if isinstance(current, dict):
                        current = current.get(key)
                        if current is None:
                            return None
                    else:
                        return None
                return current
            else:
                # 直接访问
                return data.get(rule if isinstance(rule, str) else rule)
        except:
            return None
        return None

    def _format_success_result(
        self,
        book_source: Dict[str, Any],
        config: Dict[str, Any],
        response: Dict[str, Any],
        download_url: str
    ) -> Dict[str, Any]:
        """
        格式化成功结果（美化输出）

        Args:
            book_source: 书源对象
            config: 上传配置
            response: 服务器响应
            download_url: 下载链接

        Returns:
            格式化的结果字典
        """
        return {
            'success': True,
            'message': '✅ 书源上传成功！',
            'book_source': {
                'name': book_source.get('bookSourceName', '未命名'),
                'url': book_source.get('bookSourceUrl', ''),
                'group': book_source.get('bookSourceGroup', '')
            },
            'upload_info': {
                'service': config.get('summary', '未知服务'),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'compress': config.get('compress', False)
            },
            'result': {
                'download_url': download_url,
                'raw_response': response
            },
            'usage': {
                'import_method': '方法1: 复制链接后，在阅读APP中点击"导入书源"，粘贴链接',
                'import_method_2': '方法2: 直接打开链接，长按分享到阅读APP',
                'qr_tip': '💡 提示：可以将链接生成二维码，扫描即可导入'
            }
        }


def print_upload_result(result: Dict[str, Any]):
    """
    打美化的上传结果

    Args:
        result: 上传结果字典
    """
    if result.get('success'):
        # 成功输出
        print("\n" + "=" * 60)
        print(f"  {result['message']}")
        print("=" * 60)

        # 书源信息
        print("\n📚 书源信息:")
        print(f"  名称: {result['book_source']['name']}")
        print(f"  地址: {result['book_source']['url']}")
        print(f"  分组: {result['book_source']['group']}")

        # 上传信息
        print("\n📤 上传信息:")
        print(f"  服务: {result['upload_info']['service']}")
        print(f"  时间: {result['upload_info']['timestamp']}")
        print(f"  压缩: {'是' if result['upload_info']['compress'] else '否'}")

        # 下载链接
        print("\n🔗 下载链接:")
        print(f"  {result['result']['download_url']}")

        # 使用方法
        print("\n💡 使用方法:")
        print(f"  {result['usage']['import_method']}")
        print(f"  {result['usage']['import_method_2']}")
        print(f"  {result['usage']['qr_tip']}")

        print("\n" + "=" * 60)

    else:
        # 失败输出
        print("\n" + "=" * 60)
        print("  ❌ 上传失败")
        print("=" * 60)

        print(f"\n错误: {result.get('error', '未知错误')}")
        if 'details' in result:
            print(f"详情: {result['details']}")

        print("\n" + "=" * 60)


def main():
    """命令行入口"""
    import sys

    if len(sys.argv) < 2:
        print("用法:")
        print("  python upload_book_source.py <书源JSON文件路径> [上传配置JSON文件路径]")
        print("\n示例:")
        print("  python upload_book_source.py references/book_source_database/my_source.json")
        print("  python upload_book_source.py my_source.json custom_upload_config.json")
        sys.exit(1)

    # 读取书源文件
    book_source_file = Path(sys.argv[1])
    if not book_source_file.exists():
        print(f"❌ 错误: 书源文件不存在: {book_source_file}")
        sys.exit(1)

    with open(book_source_file, 'r', encoding='utf-8') as f:
        book_source_data = json.load(f)

    # 如果是数组，取第一个元素
    if isinstance(book_source_data, list) and len(book_source_data) > 0:
        book_source = book_source_data[0]
        print(f"✓ 检测到书源数组，使用第一个书源")
    elif isinstance(book_source_data, dict):
        book_source = book_source_data
    else:
        print(f"❌ 错误: 无效的书源格式")
        sys.exit(1)

    # 读取上传配置（可选）
    upload_config = None
    if len(sys.argv) >= 3:
        config_file = Path(sys.argv[2])
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                upload_config = json.load(f)
            print(f"📝 使用自定义上传配置: {config_file}")
        else:
            print(f"⚠️  警告: 配置文件不存在，使用默认配置: {config_file}")

    # 执行上传
    uploader = BookSourceUploader()
    success, result = uploader.upload_book_source(book_source, upload_config)

    # 打印结果
    print_upload_result(result)

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
