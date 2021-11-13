# -*- coding: utf-8 -*-
# @Time    : 2021/11/13 8:24
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 002. 两数相加.py
# @Software: PyCharm 
# ===================================
"""给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
 

提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

两年前c++的代码

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int val=l1->val+l2->val;
        int flag=val/10;
        val=val%10;
        ListNode* res=new ListNode(val);
        ListNode* p=res;
        ListNode* myl1=l1;
        ListNode* myl2=l2;
        while(myl1->next&&myl2->next)
        {
            p->next=new ListNode(0);
            p=p->next;
            myl1=myl1->next;
            myl2=myl2->next;
            val=myl1->val+myl2->val+flag;
            flag=val/10;
            val=val%10;
            p->val=val;
        }
        while(myl1->next)
        {
            p->next=new ListNode(0);
            p=p->next;
            myl1=myl1->next;
            val=myl1->val+flag;
            flag=val/10;
            val=val%10;
            p->val=val;
        }
        while(myl2->next)
        {
            p->next=new ListNode(0);
            p=p->next;
            myl2=myl2->next;
            val=myl2->val+flag;
            flag=val/10;
            val=val%10;
            p->val=val;
        }
        if(flag)
        p->next=new ListNode(flag);
        return res;
    }
};
```
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        nowNode = res
        plus = 0
        while l1 and l2:
            ans = l1.val+l2.val+plus
            ans,plus = ans%10,ans//10
            nowNode.next = ListNode(ans)
            nowNode = nowNode.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            ans = l1.val+plus
            ans,plus = ans%10,ans//10
            nowNode.next = ListNode(ans)
            nowNode = nowNode.next
            l1 = l1.next

        while l2:
            ans = l2.val+plus
            ans,plus = ans%10,ans//10
            nowNode.next = ListNode(ans)
            nowNode = nowNode.next
            l2 = l2.next

        if plus:
            nowNode.next = ListNode(1)

        return res.next


def test(data_test):
    s = Solution()
    return s.addTwoNumbers(*data_test)


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