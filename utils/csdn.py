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

SRC_DIR = Path(r'..\code')
OUT_DIR = Path(r'..\doc\csdn')
CHECK_DIR = Path(r'..\doc\csdn\已发表')

LEVEL_NAME_DICT = {
    'AC1_easy': '简单',
    'AC2_normal': '普通',
    'AC3_hard': '困难',
    'Interview': '面试题',
    'Offer': '剑指 Offer',
}


def Get标题(filestem, level_name):
    filestem = str(filestem)
    if 'Offer_' in filestem:
        filestem = 'Offer_' + filestem[12:]
    return f'模拟卷Leetcode【{level_name}】{filestem}'


def Get文件名(filestem, out_dir=OUT_DIR, levelname='levelname'):
    filestem = str(filestem)
    if 'Offer_' in filestem:
        filestem = 'Offer_' + filestem[12:]
    elif ' ' in filestem:
        filestem = filestem.replace(' ',f'【{levelname}】',1)

    outpath = out_dir / f'{filestem}.md'
    return outpath


def GetDetail(filepath):
    """题目名字, 题目说明, 代码"""
    题目名字 = filepath.stem
    with open(filepath, 'r', encoding='utf-8') as file:
        datalines = file.readlines()

    # 找题目说明：第一个和第二个"""
    first_second, cnt, id = [], 0, 0
    while cnt < 2:
        if '"""' in datalines[id]:
            first_second.append(id)
            cnt += 1
        id += 1
    if cnt == 2:
        题目说明 = datalines[first_second[0]:first_second[1]]
        题目说明[0] = 题目说明[0][3:]
        题目说明 = ''.join(题目说明)
        代码 = ''.join(datalines[first_second[1] + 1:])
    else:
        题目说明 = '（题目说明未记录）'
        代码 = ''.join(datalines[8:])
    # print('题目说明')
    # print(题目说明)
    # print('代码')
    # print(代码)

    return 题目名字, 题目说明, 代码


def GetResult(标题, 题目名字, 题目说明, 代码):
    res = f"""

## 汇总：[模拟卷Leetcode 题解汇总](https://blog.csdn.net/qq_34451909/article/details/120968335)
    
### 标题

```
{标题}
```



### 正文

```
### {题目名字}

{题目说明}



代码：

​```python
{代码}
​```

备注：
GitHub：[https://github.com/monijuan/leetcode_python ](https://github.com/monijuan/leetcode_python)

CSDN汇总：[模拟卷Leetcode 题解汇总](https://blog.csdn.net/qq_34451909/article/details/120968335)

可以加QQ群交流：==*1092754609*==

> leetcode_python.utils详见汇总页说明
> 先刷的题，之后用脚本生成的blog，如果有错请留言，我看到了会修改的！谢谢！

```
    """
    return res


def WriteFile(out, path):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(out)


def 未发表(filestem, check_dir=CHECK_DIR, levelname=''):
    checkpath = check_dir / Get文件名(filestem,levelname=levelname).name
    return not (checkpath.is_file() or Get文件名(filestem,levelname=levelname).is_file())


def main(checkold=True, choicelevel = []):
    cnt_all, cnt_new = 0, 0
    for sub_dir in SRC_DIR.glob('**'):
        # print('-'*50)
        if sub_dir != SRC_DIR:
            level_name = LEVEL_NAME_DICT.get(sub_dir.name, '其他')
            # if level_name != '剑指 Offer':continue
            if len(choicelevel) and level_name not in choicelevel:
                print(f'跳过【{level_name}】')
                continue
            for filepath in sub_dir.glob('*.py'):
                # print('-'*50)
                # print(filepath)
                cnt_all += 1

                if not checkold or 未发表(filestem=filepath.stem,levelname=level_name):
                    cnt_new += 1
                    题目名字, 题目说明, 代码 = GetDetail(filepath)
                    标题 = Get标题(filestem=filepath.stem, level_name=level_name)
                    outpath = Get文件名(filestem=filepath.stem,levelname=level_name)
                    out = GetResult(标题, 题目名字, 题目说明, 代码)
                    WriteFile(out,outpath)

                    # print('标题',标题)
                    # print('题目名字',题目名字)
                    # print('outpath',outpath)
                    print(f'成功转换：{outpath}')
                else:
                    print(f'已存在：{filepath.stem}')
    if checkold:
        print(f'已有转换：{cnt_all - cnt_new}，新转换：{cnt_new}，累计：{cnt_all}！')
    else:
        print(f'未开启检查已转换文件，本次一共转换：{cnt_all}！')


if __name__ == '__main__':
    main(checkold=True,choicelevel=['普通'])
