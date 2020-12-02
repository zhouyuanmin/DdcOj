"""
1、需要先初始化python环境:
- pip install requirements.txt
2、对python的环境执行mock操作
3、配合java环境
"""
import shutil
import sys
import os
from typing import Dict

# 配置mock文件链接, 库地址:../python3.6/site-packages
mock_file_links = {
    # mock函数:scatter(散点图评测)
    '_axes_copy.py': 'matplotlib/axes/_axes.py',
}


def mock(links: Dict):
    """
    对python的环境执行mock操作
    """
    # 获取python存放第三方库的目录路径
    packages_dir: str
    for path in sys.path:
        if 'packages' in path:
            packages_dir = path
            break
    else:
        raise FileNotFoundError("Can't find site packages path")

    # 获取存放mock文件的目录路径
    this_dir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
    mock_dir = os.path.join(this_dir, 'mock')

    # 执行文件mock操作
    for src, dst in links.items():
        src_file = os.path.join(mock_dir, src)
        dst_file = os.path.join(packages_dir, dst)
        # 文件必须存在, 确保第三方库已安装
        if not os.path.isfile(dst_file):
            raise FileNotFoundError(f"No such file: '{dst_file}'")
        else:
            # 先删除，再复制
            os.remove(dst_file)
            shutil.copyfile(src_file, dst_file)
            print(f"INFO: The file '{dst}' was replaced successfully")


# 配合java环境
def adapt_java():
    # setting:
    # java执行目录路径
    java_cwd_dir = '/opt'
    this_dir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))

    # 复制字体
    fonts_dir = os.path.join(this_dir, 'resources/fonts')
    font_suffixes = ['.ttf', '.otf']
    for file in os.listdir(fonts_dir):
        if os.path.splitext(file)[-1] in font_suffixes:
            src_file = os.path.join(fonts_dir, file)
            dst_file = os.path.join(java_cwd_dir, file)
            # 复制, 如果存在, 则需要先删除
            if os.path.isfile(file):
                os.remove(file)
            shutil.copyfile(src_file, dst_file)

# 执行mock函数
# mock(mock_file_links)
# 配合java环境
# adapt_java()
