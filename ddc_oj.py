"""
TODO:所有的评测都是执行这个文件，通过参数 --oj 来确定测评的内容
"""
import os
import sys
import json
import shutil
import subprocess
from pathlib import Path
from tempfile import mkstemp
from typing import Dict, List


def word_cloud_oj(
        code: str,
        answer: Dict,
        scores: Dict,
        match: float = 1.0,
        debug: bool = False
):
    tmp_fp, tmp_file_name = mkstemp(
        suffix=".py",
        prefix='tmp_',
        dir='/tmp',
        text=True
    )
    try:
        # code 必须是 str 才能写入文件
        with open(tmp_file_name, 'w') as f:
            f.write(code)
        # 创建子进程执行代码
        cmd = ['python', '-sB', tmp_file_name]
        process = subprocess.Popen(
            args=cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            close_fds=True
        )
        # 评测词云，打分
        score = 0
        while True:
            try:
                line_data: bytes = process.stdout.readline()
                if not line_data:
                    break
                if b'e485c73f5dd07c29' in line_data:
                    review_data: str = line_data.decode('u8')
                    review_data: Dict = json.loads(review_data)
                    if debug:
                        print(f'debug:review_data-->{review_data}')
                    for key, value in answer.items():
                        # 字符串或数值，则比较值是否相等
                        if isinstance(value, (str, int)):
                            tmp_score = scores.get(key) if value == review_data.get(key, None) else 0
                        elif isinstance(value, List):
                            tmp_score = scores.get(key) if set(value) == set(review_data.get(key, None)) else 0
                        elif isinstance(value, Dict):
                            tmp_score = scores.get(key) if value == review_data.get(key, None) else 0
                        else:
                            tmp_score = 0
                        score += tmp_score
                else:
                    if debug:
                        print(f'debug:line_data-->{line_data.decode("u8")}')  # 打印其他数据
            except TimeoutError:
                lines_data: bytes = process.stdout.read(1024)
                if debug:
                    print(f'debug:lines_data-->{lines_data.decode("u8")}')  # 数据不是多行，不走这里

        # 还原环境，删除临时文件
        os.remove(tmp_file_name)

        # 返回结果
        result = {"msg": "False",
                  "code": 0,
                  "data": {}}
        if score / 100 >= match:
            result = {
                "msg": "True",
                "code": 1,
                "data": {}
            }
            return result
    finally:
        # 还原环境，删除临时文件
        os.remove(tmp_file_name)


