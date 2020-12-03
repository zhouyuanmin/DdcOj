# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
# -*- coding: utf-8 -*-                            |
# @Time    : 2020/11/25 9:33                       *
# @Author  : Bob He                                |
# @FileName: matplotlib_oj.py                      *
# @Software: PyCharm                               |
# @Project : ddc_oj                                *
# @Csdn    ：https://blog.csdn.net/bobwww123       |
# @Github  ：https://www.github.com/NocoldBob      *
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
import sys
import os
import json
import subprocess
import shutil
from typing import Dict
from pathlib import Path
from tempfile import mkdtemp, mkstemp


def get_data(code: str):
    # 生成文件
    tmp_dir = mkdtemp(dir="/tmp")
    tmp_fp, tmp_file_name = mkstemp(suffix=".py", text=True, dir=tmp_dir)
    with open(tmp_file_name, "w") as f:
        f.write('import random;random.seed(1);')
        f.write(code)

    # 子进程执行文件
    cmd = ["python", "-IB", tmp_file_name]
    cmd = " ".join(cmd)
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    while True:
        buff = pipe.stdout.readline()
        if b'29121bda1632e861' in buff:  # ScatterDate的md5是29121bda1632e861
            break
        elif b'' == buff:
            break

    scatter_date: dict = json.loads(buff.decode('u8'))
    x = scatter_date.get('x')
    y = scatter_date.get('y')
    return scatter_date


def review_matplotlib(code: str, answer: Dict, scores: Dict, debug: False, match: float = 1.0):
    scatter_date = get_data(code)
    if debug:
        print(scatter_date)
    score = 0
    # 测评直方图
    if 'height' in scatter_date.keys():
        if answer.get('x') == scatter_date.get('x'):
            score += scores.get('x')
        if answer.get('height') == scatter_date.get('height'):
            score += scores.get('height')
        result = {"code": 0, "msg": "False", "data": {}}
        if score / 100 >= match:
            result = {
                "code": 1,
                "msg": "True",
                "data": {}
            }
        return result
    else:
        if answer.get('x') == scatter_date.get('x'):
            score += scores.get('x')
        if answer.get('y') == scatter_date.get('y'):
            score += scores.get('y')
        result = {"code": 0, "msg": "False", "data": {}}
        if score / 100 >= match:
            result = {
                "code": 1,
                "msg": "True",
                "data": {}
            }
        return result
