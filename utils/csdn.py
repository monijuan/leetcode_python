# -*- coding: utf-8 -*-
# @Time    : 2021/10/21 11:22
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : csdn.py
# @Software: PyCharm
# ===================================
from pathlib import Path
import os
import sys

LEVEL_NAME_DICT = {
    'AC1_easy':'简单',
    'AC2_normal':'普通',
    'AC3_hard':'困难',
    'Interview':'面试题',
    'Offer':'剑指 Offer',
}

def GetTitle(level_name,filestem):
    return f'模拟卷Leetcode【{level_name}】{filestem}'


def GetResult():
    res = """
    """



def main():
    src_dir = Path(r'D:\YZJ\file\work\202108 codeTest\leetcode_python\code')
    out_dir = Path(r'D:\YZJ\file\work\202108 codeTest\leetcode_python\doc\csdn')

    for sub_dir in src_dir.glob('**'):
        print(sub_dir)
        if sub_dir != src_dir:
            level_name = LEVEL_NAME_DICT.get(sub_dir.name,'其他')
            for filepath in sub_dir.glob('*.py'):
                filename = filepath.name

                title = GetTitle(level_name = level_name, filestem = filepath.stem)
                print(title)


if __name__ == '__main__':
    main()
