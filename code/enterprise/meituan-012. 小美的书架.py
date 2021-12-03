# -*- coding: utf-8 -*-
# @Time    : 2021/12/3 10:34
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : meituan-012. 小美的书架.py
# @Software: PyCharm
# ===================================
"""小美的书架上有很多书。小美是个爱读书的新时代好青年。
小团虽然也喜欢看书，但小团大多数时候都更喜欢来小美家蹭书读。
这就导致小美的书架上很多书都会被小团借走。
小美很烦这一点，就想出了一个招数，小美的书架是一行一行的，他会对一些行加锁，这样小团就借不走了。
现在小团想要借书，请你帮忙看看小团能不能借到书，如果可以借到的话在哪一行书架上有这本书。
为了简单起见，每本书将用一个正整数进行编号，小美的书架一共有 N 行。

格式：


输入：
- 第一行三个正整数 M，N，Q，表示小美书架有 N 行编号 1 到 N ，书本编号从 1 到 M ，接下来有 Q 个操作
- 接下来 Q 行，每行是下列操作中的一种：
  1. x y : x 是书本的编号，y 是书架的行编号，代表小美将编号为 x 的书本放置到 y 行上。若该书本在小团手上则放置无效，若原来该书在书架上且原行上锁则放置无效，若该书被放置到一个锁了的行上则放置无效。
  2. y : y 是书架的行编号，代表小美将行编号为 y 的书架加锁，对已经上锁的书架行该操作无效。
  3. y : y 是书架的行编号，代表小美将行编号为 y 的书架锁去掉，对无锁的书架行该操作无效。
  4. x : x 是书本的编号，代表小团想借编号为 x 的书本，对该操作若可以借到输出一行正整数在哪一行，借不到输出一行 -1
  5. x : x 是书本的编号，代表小团还回来编号为 x 的书本。若该书本不在小团手上该操作无效。
输出：
- 对于每个操作 4 ，若可以借到输出一行正整数在哪一行，借不到输出一行 -1 。
示例：


输入：
     5 5 10
     1 1 4
     1 2 3
     1 3 1
     2 1
     4 1
     5 2
     4 3
     4 5
     3 1
     4 2
输出：
     4
     -1
     -1
     3
提示：

对于 30% 的数据有 N<=10, M<=10, Q<=20
对于 80% 的数据有 N<=1000, M<=1000, Q<=100000
对于 100% 的数据有 N<=10000, M<=10000, Q<=100000
请注意，本题需要自行编写「标准输入」和「标准输出」逻辑，以及自行 import/include 需要的 library。了解书写规则

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/FvoBGh
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


"""
会遇到的各种问题：

- 注意numbook,numrow的输入顺序
- 借书还书可能不在范围内
- 还书不还到原来书架位置
"""


class Bookshelf:
    def __init__(self,numRow,numBook):
        self.shelf_locked = [False]*(numRow+1)
        self.book_shelf = {}
        self.book_lent = [False]*(numBook+1)

    def fun1(self, bookId, shelfId):
        """把 bookId的书 放到 shelfId架子上"""
        if self.book_lent[bookId]:return        # 借出了
        if self.shelf_locked[shelfId]:return    # 原来行上锁了
        bookshelf = self.book_shelf.get(bookId,None)
        if bookshelf and self.shelf_locked[bookshelf]:return    # 这行上锁了
        self.book_shelf[bookId] = shelfId

    def fun2(self, shelfId):
        """把 shelfId架子 关锁"""
        self.shelf_locked[shelfId] = True

    def fun3(self, shelfId):
        """把 shelfId架子 开锁"""
        self.shelf_locked[shelfId] = False

    def fun4(self, bookId):
        """把 bookId书 借出"""
        bookshelf = self.book_shelf.get(bookId,None)
        if self.book_lent[bookId] or not bookshelf or self.shelf_locked[bookshelf]:
            print(-1)
        else:
            self.book_lent[bookId] = True
            print(bookshelf)

    def fun5(self, bookId):
        """把 bookId书 还入"""
        if self.book_lent[bookId]:
            self.book_lent[bookId] = False
            self.book_shelf[bookId] = None

if __name__ == '__main__':
    numbook,numrow,Q = list(map(int,input().split()))
    bookshelf = Bookshelf(numrow,numbook)
    while Q:
        q = list(map(int,input().split()))
        bookshelf.__getattribute__(f'fun{q.pop(0)}')(*q)
        Q-=1

