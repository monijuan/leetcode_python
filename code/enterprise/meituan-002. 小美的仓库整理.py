# -*- coding: utf-8 -*-
# @Time    : 2021/11/28 10:03
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : meituan-002. 小美的仓库整理.py
# @Software: PyCharm
# ===================================
"""小美是美团仓库的管理员，她会根据单据的要求按顺序取出仓库中的货物，每取出一件货物后会把剩余货物重新堆放，使得自己方便查找。已知货物入库的时候是按顺序堆放在一起的。如果小美取出其中一件货物，则会把货物所在的一堆物品以取出的货物为界分成两堆，这样可以保证货物局部的顺序不变。
已知货物最初是按 1~n 的顺序堆放的，每件货物的重量为 w[i] ,小美会根据单据依次不放回的取出货物。请问根据上述操作，小美每取出一件货物之后，重量和最大的一堆货物重量是多少？

格式：


输入：
- 输入第一行包含一个正整数 n ，表示货物的数量。
- 输入第二行包含 n 个正整数，表示 1~n 号货物的重量 w[i] 。
- 输入第三行有 n 个数，表示小美按顺序取出的货物的编号，也就是一个 1~n 的全排列。
输出：
- 输出包含 n 行，每行一个整数，表示每取出一件货物以后，对于重量和最大的一堆货物，其重量和为多少。
示例：


输入：
     5
     3 2 4 4 5
     4 3 5 2 1
输出：
     9
     5
     5
     3
     0
解释：
原本的状态是 {{3,2,4,4,5}} ，取出 4 号货物后，得到 {{3,2,4},{5}} ，第一堆货物的和是 9 ，然后取出 3 号货物得到 {{3,2}{5}} ，此时第一堆和第二堆的和都是 5 ，以此类推。
提示：

1 <= n <= 50000
1 <= w[i] <= 100
请注意，本题需要自行编写「标准输入」和「标准输出」逻辑，以及自行 import/include 需要的 library。了解书写规则

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/TJZLyC
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

### 测试case

"""
5
3 2 4 4 5
4 3 5 2 1
"""

"""
1
5
1
"""

"""
7
45 23 34 12 11 11 3
2 1 4 6 3 7 5
"""

num = int(input())
if num>1:
    weights = list(map(int,input().split()))
    splitids = list(map(lambda x:int(x)-1,input().split()))
    id_range_dict = {}
    max_now = 0
    res = [0 for _ in range(num)]
    for id in range(num-1,-1,-1):
        # 当前位置的结果是插入之前的最大值
        res[id] = max_now
        index_now = splitids[id]
        weight_now = weights[index_now]
        left_now,right_now = index_now-1,index_now+1

        # 更新插入这个点后最大堆
        if left_now in id_range_dict and right_now in id_range_dict:        # [......,new,......]
            ll,lr,lres = id_range_dict[left_now]
            rl,rr,rres = id_range_dict[right_now]#找出左右两边的区间
            id_range_dict.pop(lr)
            id_range_dict.pop(rl)   # 删除中间两个端点
            id_range_dict[ll] = id_range_dict[rr] = (ll,rr,lres+rres+weight_now) # 更新两端
            max_now = max(max_now,id_range_dict[ll][2])   # 更新最大值
        elif left_now in id_range_dict:                                     # [......,new]
            ll,lr,lres = id_range_dict[left_now]
            id_range_dict.pop(lr)
            id_range_dict[ll] = id_range_dict[index_now] = (ll,index_now,lres+weight_now) # 更新两端
            max_now = max(max_now, id_range_dict[index_now][2])   # 更新最大值
        elif right_now in id_range_dict:                                    # [new,......]
            rl,rr,rres = id_range_dict[right_now]
            id_range_dict.pop(rl)
            id_range_dict[rr] = id_range_dict[index_now] = (index_now,rr,rres+weight_now) # 更新两端
            max_now = max(max_now, id_range_dict[index_now][2])   # 更新最大值
        else:
            id_range_dict[index_now] = (index_now,index_now,weight_now)     # [new]
            max_now = max(max_now,weight_now)   # 更新最大值
    print('\n'.join(str(x) for x in res))

else:
    w = int(input())
    i = int(input())
    print(0)