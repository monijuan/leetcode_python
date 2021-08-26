# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 17:18
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : 138. 复制带随机指针的链表.py
# @Software: PyCharm
# ===================================
"""给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。

返回复制链表的头节点。

用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
你的代码 只 接受原链表的头节点 head 作为传入参数。

 

示例 1：



输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：



输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
示例 3：



输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
 

提示：

0 <= n <= 1000
-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/copy-list-with-random-pointer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import copy
import time
from typing import List

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)   # value
        self.next = next
        self.random = random

    def __str__(self):
        return f'val:{None if self.val is None else self.val}, ' \
               f'next:{None if self.next is None else self.next.val}, ' \
               f'random:{None if self.random is None else self.random.val}, '

    # def __copy__(self, node:'Node'):
    #     self.val = node.val
    #     self.next = node.next
    #     self.random = node.random

class Solution:
    def __init__(self):
        self.nodes = {}

    def __show(self):
        print('-='*50)
        print(type(self.nodes))
        print(self.nodes)
        for key,node in self.nodes.items():
            print(key,node)
        print('--'*50)

    def dfs(self,node):
        if not node:return None
        elif node in self.nodes:return self.nodes[node]

        new = Node(node.val)
        self.nodes[node] = new
        new.next = self.dfs(node.next)
        new.random = self.dfs(node.random)
        return new

    def copyRandomList(self, head: 'Node') -> 'Node':
        res =  self.dfs(head)
        # self.__show()
        return res


def test(data_test):
    s = Solution()
    node_list = []
    for pair in data_test:
        node = Node(pair[0], None, None)
        node_list.append(node)
    for id in range(len(data_test)):
        node_list[id].next = None if id==len(data_test)-1 else node_list[id+1]
        node_list[id].random = None if data_test[id][1] is None  else node_list[data_test[id][1]]

    return s.copyRandomList(node_list[0])


if __name__ == '__main__':
    datas = [
        [[7,None],[13,0],[11,4],[10,2],[1,0]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
