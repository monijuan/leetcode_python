# -*- coding: utf-8 -*-
# @Time    : 2021/9/24 11:20
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 297. 二叉树的序列化与反序列化.py
# @Software: PyCharm
# ===================================
"""序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

 

示例 1：


输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：

输入：root = [1,2]
输出：[1,2]
 

提示：

树中结点数在范围 [0, 104] 内
-1000 <= Node.val <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

import collections
# 测试case
"""
[1,2,3,null,null,4,5]
[]
[1]
[1,2]
[-1,0,1]
[5,2,3,null,null,2,4,3,1]
"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = collections.deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('None')
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        dataList = data[1:-1].split(',')
        root = TreeNode(int(dataList[0]))
        queue = collections.deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if dataList[i] != 'None':
                node.left = TreeNode(int(dataList[i]))
                queue.append(node.left)
            i += 1
            if dataList[i] != 'None':
                node.right = TreeNode(int(dataList[i]))
                queue.append(node.right)
            i += 1
        return root


class Codec_暴力超时:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        print('serialize')
        print('serialize root', root)
        if not root: return []
        res = []
        cnt_need_pop = 1
        queue_node = [root]
        while cnt_need_pop:
            node = queue_node.pop(0)
            if node:
                res.append(node.val)
                cnt_need_pop -= 1
                if node.left:
                    cnt_need_pop += 1
                    queue_node.append(node.left)
                else:
                    queue_node.append(None)
                if node.right:
                    cnt_need_pop += 1
                    queue_node.append(node.right)
                else:
                    queue_node.append(None)
            else:
                res.append(None)
                queue_node.append(None)
                queue_node.append(None)
        print('serialize res', res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        print('deserialize')
        print('deserialize data',data)

        length = len(data)
        if not length:return None
        node_list = [TreeNode(x) if x is not None else None for x in data]
        for i,node in enumerate(node_list):
            if node:
                if 2*i+1<length: node.left=node_list[2*i+1]
                if 2*i+2<length: node.right=node_list[2*i+2]
            if 2*i>length:break

        root = node_list[0]
        print('deserialize root',root)
        return root



def test(data_test):
    s = Solution()
    return s.getResult(*data_test)


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
        [],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
