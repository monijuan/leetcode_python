# -*- coding: utf-8 -*-
# @Time    : 2021/9/9 8:48
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 068. 文本左右对齐.py
# @Software: PyCharm
# ===================================
"""给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/text-justification
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def selectLineRight(self,line_left)->int:
        """一行放得下第 line_left 个word到第 res 个word"""
        width = len(self.words[line_left])
        while line_left+1<self.num_words and width+len(self.words[line_left+1])+1<=self.max_width:
            width+=len(self.words[line_left+1])+1
            line_left+=1
        return line_left

    def makeLineString(self,left,right,isLastLine):
        if isLastLine:
            thisline = ' '.join(self.words[left:right+1])
            thisline += ' '*(self.max_width-len(thisline))
        else:
            num_space_need = self.max_width-len(''.join(self.words[left:right+1]))
            num_space = right-left
            if num_space>0: # 如果一行单词个数超过一个，需要计算中间的空格
                space = [num_space_need//num_space for _ in range(num_space)]
                num_space_remain = num_space_need%num_space
                for i in range(num_space_remain):
                    space[i]+=1
                space.append(0)
            else:   # 如果这一行只能放下一个单词，需要计算后面有多少个空格
                space=[self.max_width-len(self.words[left]),0]
            thisline = ''
            for id in range(left,right+1):
                thisline = thisline+self.words[id] + ' '*space[id-left]
        self.res.append(thisline)

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        self.num_words = len(words)
        self.words = words
        self.max_width = maxWidth

        # 把每一行应该有的word分开
        res_ids = []
        line_left = 0
        while line_left < self.num_words:
            line_right = self.selectLineRight(line_left)
            res_ids.append([line_left, line_right])
            line_left = line_right+1

        # 组织每一行的单词
        for id,left_right in enumerate(res_ids):
            self.makeLineString(*left_right,id==len(res_ids)-1)

        for x in self.res:
            print(x)
        return self.res


def test(data_test):
    s = Solution()
    return s.fullJustify(*data_test)


def test_obj(data_test):
    result = [None]
    obj = Solution(*data_test[1][0])
    for fun, data in zip(data_test[0][1::], data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
    return result


if __name__ == '__main__':
    datas = [
        [["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],20],
        # [["What","must","be","acknowledgment","shall","be"],16],
        # [["This", "is", "an", "example", "of", "text", "justification."],16],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
