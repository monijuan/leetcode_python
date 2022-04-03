# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 10:28
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5302AC. 加密解密字符串.py
# @Software: PyCharm 
# ===================================
"""给你一个字符数组 keys ，由若干 互不相同 的字符组成。还有一个字符串数组 values ，内含若干长度为 2 的字符串。另给你一个字符串数组 dictionary ，包含解密后所有允许的原字符串。请你设计并实现一个支持加密及解密下标从 0 开始字符串的数据结构。

字符串 加密 按下述步骤进行：

对字符串中的每个字符 c ，先从 keys 中找出满足 keys[i] == c 的下标 i 。
在字符串中，用 values[i] 替换字符 c 。
字符串 解密 按下述步骤进行：

将字符串每相邻 2 个字符划分为一个子字符串，对于每个子字符串 s ，找出满足 values[i] == s 的一个下标 i 。如果存在多个有效的 i ，从中选择 任意 一个。这意味着一个字符串解密可能得到多个解密字符串。
在字符串中，用 keys[i] 替换 s 。
实现 Encrypter 类：

Encrypter(char[] keys, String[] values, String[] dictionary) 用 keys、values 和 dictionary 初始化 Encrypter 类。
String encrypt(String word1) 按上述加密过程完成对 word1 的加密，并返回加密后的字符串。
int decrypt(String word2) 统计并返回可以由 word2 解密得到且出现在 dictionary 中的字符串数目。


示例：

输入：
["Encrypter", "encrypt", "decrypt"]
[[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]
输出：
[null, "eizfeiam", 2]

解释：
Encrypter encrypter = new Encrypter([['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]);
encrypter.encrypt("abcd"); // 返回 "eizfeiam"。
                           // 'a' 映射为 "ei"，'b' 映射为 "zf"，'c' 映射为 "ei"，'d' 映射为 "am"。
encrypter.decrypt("eizfeiam"); // return 2.
                              // "ei" 可以映射为 'a' 或 'c'，"zf" 映射为 'b'，"am" 映射为 'd'。
                              // 因此，解密后可以得到的字符串是 "abad"，"cbad"，"abcd" 和 "cbcd"。
                              // 其中 2 个字符串，"abad" 和 "abcd"，在 dictionary 中出现，所以答案是 2 。


提示：

1 <= keys.length == values.length <= 26
values[i].length == 2
1 <= dictionary.length <= 100
1 <= dictionary[i].length <= 100
所有 keys[i] 和 dictionary[i] 互不相同
1 <= word1.length <= 2000
1 <= word2.length <= 200
所有 word1[i] 都出现在 keys 中
word2.length 是偶数
keys、values[i]、dictionary[i]、word1 和 word2 只含小写英文字母
至多调用 encrypt 和 decrypt 总计 200 次
"""
from leetcode_python.utils import *

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.dictionary = dictionary
        self.enc_map = {}
        for k,v in zip(keys,values):
            self.enc_map[k]=v
        self.cnt_dec = defaultdict(int)
        for di in dictionary:
            self.cnt_dec[self.encrypt(di)]+=1

    def encrypt(self, word1: str) -> str:
        res = ''
        for c in word1:
            res += self.enc_map.get(c,c)
        return res

    def decrypt(self, word2: str) -> int:
        return self.cnt_dec[word2]


class Encrypter_tle:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.dictionary = dictionary
        self.enc_map = {}
        self.dec_map = defaultdict(list)
        for k, v in zip(keys, values):
            self.enc_map[k] = v
            self.dec_map[v].append(k)
        self.cnt_dec = defaultdict(int)

    def encrypt(self, word1: str) -> str:
        res = ''
        for c in word1:
            res += self.enc_map.get(c, c)
        return res

    def decrypt_tle_dfs(self, word2: str) -> int:
        l = len(word2)
        def dfs(i,word):
            if i>=l:
                return int(word in self.dictionary)
            else:
                res = 0
                for app in self.dec_map[word2[i:i + 2]]:
                    res+=dfs(i+2,word+app)
                return res
        return dfs(0,'')

    def decrypt_tle(self, word2: str) -> int:
        res = self.dec_map[word2[0:2]]
        for i in range(2,len(word2),2):
            new = []
            for r in res:
                for app in self.dec_map[word2[i:i+2]]:
                    new.append(r+app)
            res = new
        print(res)
        return len([r for r in res if r in self.dictionary])



def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.getResult(*data)

def test_obj(data_test):
    result = [None]
    obj = Encrypter(*data_test[1][0])
    for fun,data in zip(data_test[0][1::],data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
    return result

if __name__ == '__main__':
    datas = [
        [["Encrypter","encrypt","decrypt"],[[["a","b","c","d"],["ei","zf","ei","am"],["abcd","acbd","adbc","badc","dacb","cadb","cbda","abad"]],["abcd"],["eizfeiam"]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test_obj(data_test))
        print(f'use time:{time.time() - t0}s')
