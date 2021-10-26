### 标题

```
模拟卷Leetcode【剑指 Offer】Offer_12. 矩阵中的路径
```



### 正文

```
### Offer_day14_12. 矩阵中的路径

给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。



 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
 

提示：

1 <= board.length <= 200
1 <= board[i].length <= 200
board 和 word 仅由大小写英文字母组成
 

注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




代码：

​```python
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def dfs(self, visited,row_id,col_id,word_id):
        if row_id<0 or row_id>=self.height or \
                col_id<0 or col_id>=self.width or \
                self.word[word_id]!=self.board[row_id][col_id] or \
                visited[row_id][col_id]:
            return False
        elif word_id==len(self.word)-1:
            return True
        else:
            visited[row_id][col_id]=True
            res = self.dfs(visited, row_id + 1, col_id, word_id+1) or \
                  self.dfs(visited, row_id - 1, col_id, word_id + 1) or \
                  self.dfs(visited, row_id, col_id + 1, word_id + 1) or \
                  self.dfs(visited, row_id, col_id - 1, word_id + 1)
            visited[row_id][col_id]=False
            return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board)==0 or len(board[0])==0 :return False
        self.board = board
        self.height = len(board)
        self.width = len(board[0])
        self.word = word
        visited=[[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for row_id,row in enumerate(board):
            for col_id,item in enumerate(row):
                if self.dfs(visited,row_id,col_id,0):
                    return True
        return False


def test(data_test):
    s = Solution()
    return s.exist(*data_test)


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
        [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"],
        # [[["a"]],"a"],
        # [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"],
        # [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

​```

备注：
GitHub：[https://github.com/monijuan/leetcode_python ](https://github.com/monijuan/leetcode_python)

CSDN汇总：[模拟卷Leetcode 题解汇总_卷子的博客-CSDN博客](https://blog.csdn.net/qq_34451909/article/details/120968335)

可以加QQ群交流：==*1092754609*==

> leetcode_python.utils详见汇总页说明
> 先刷的题，之后用脚本生成的blog，如果有错请留言，我看到了会修改的！谢谢！

```
    