# -*- coding: utf-8 -*-
# @Time    : 2021/12/25 22:02
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5947AC. 从给定原材料中找到所有可以做出的菜.py
# @Software: PyCharm 
# ===================================
"""你有 n 道不同菜的信息。给你一个字符串数组 recipes 和一个二维字符串数组 ingredients 。第 i 道菜的名字为 recipes[i] ，如果你有它 所有 的原材料 ingredients[i] ，那么你可以 做出 这道菜。一道菜的原材料可能是 另一道 菜，也就是说 ingredients[i] 可能包含 recipes 中另一个字符串。

同时给你一个字符串数组 supplies ，它包含你初始时拥有的所有原材料，每一种原材料你都有无限多。

请你返回你可以做出的所有菜。你可以以 任意顺序 返回它们。

注意两道菜在它们的原材料中可能互相包含。



示例 1：

输入：recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
输出：["bread"]
解释：
我们可以做出 "bread" ，因为我们有原材料 "yeast" 和 "flour" 。
示例 2：

输入：recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
输出：["bread","sandwich"]
解释：
我们可以做出 "bread" ，因为我们有原材料 "yeast" 和 "flour" 。
我们可以做出 "sandwich" ，因为我们有原材料 "meat" 且可以做出原材料 "bread" 。
示例 3：

输入：recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
输出：["bread","sandwich","burger"]
解释：
我们可以做出 "bread" ，因为我们有原材料 "yeast" 和 "flour" 。
我们可以做出 "sandwich" ，因为我们有原材料 "meat" 且可以做出原材料 "bread" 。
我们可以做出 "burger" ，因为我们有原材料 "meat" 且可以做出原材料 "bread" 和 "sandwich" 。
示例 4：

输入：recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast"]
输出：[]
解释：
我们没法做出任何菜，因为我们只有原材料 "yeast" 。


提示：

n == recipes.length == ingredients.length
1 <= n <= 100
1 <= ingredients[i].length, supplies.length <= 100
1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
recipes[i], ingredients[i][j] 和 supplies[k] 只包含小写英文字母。
所有 recipes 和 supplies 中的值互不相同。
ingredients[i] 中的字符串互不相同。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        set_sup =  set(supplies)
        dict_need = defaultdict(set)
        for rec,ing in zip(recipes,ingredients):
            dict_need[rec] = set(ing)-set_sup
        res = []
        goon = True
        while goon or any([len(v)==0 for v in dict_need.values()]):
            goon=False
            dict_need_new = defaultdict(set)
            for rec,need in dict_need.items():
                if len(need)==0:
                    res.append(rec)
                    set_sup.add(rec)
                    goon=True
                else:
                    dict_need_new[rec]=need-set_sup
            dict_need = dict_need_new
        # for x,y in dict_need.items():
        #     print(x,y)
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.findAllRecipes(*data)


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
        # [["bread"],[["yeast","flour"]],["yeast","flour","corn"]],
        # [["bread","sandwich"],[["yeast","flour"],["bread","meat"]],["yeast","flour","meat"]],
        [["g","dfk","diyob","kkx","or","qniq","qhy","b","jk","rcy"],
[["eescu","in","hbgw","ardh","ii","om"],["ii","ardh","in","hbgw"],["ardh","rcy"],["ardh","ii","eescu","hbgw","rcy","jk","b"],["hbgw","ii","in","ardh","om"],["gjotw"],["in","ardh","hbgw","om","ii","kkx","qniq"],["om","hbgw","ii","ardh","in","eescu"],["ii","om","hbgw","eescu"],["om","hbgw","in","ardh","eescu"]],
["om","hbgw","in","ardh","eescu","ii"]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')