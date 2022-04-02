# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 16:09
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1797. 设计一个验证系统.py
# @Software: PyCharm 
# ===================================
"""你需要设计一个包含验证码的验证系统。每一次验证中，用户会收到一个新的验证码，这个验证码在 currentTime 时刻之后 timeToLive 秒过期。如果验证码被更新了，那么它会在 currentTime （可能与之前的 currentTime 不同）时刻延长 timeToLive 秒。

请你实现 AuthenticationManager 类：

AuthenticationManager(int timeToLive) 构造 AuthenticationManager 并设置 timeToLive 参数。
generate(string tokenId, int currentTime) 给定 tokenId ，在当前时间 currentTime 生成一个新的验证码。
renew(string tokenId, int currentTime) 将给定 tokenId 且 未过期 的验证码在 currentTime 时刻更新。如果给定 tokenId 对应的验证码不存在或已过期，请你忽略该操作，不会有任何更新操作发生。
countUnexpiredTokens(int currentTime) 请返回在给定 currentTime 时刻，未过期 的验证码数目。
如果一个验证码在时刻 t 过期，且另一个操作恰好在时刻 t 发生（renew 或者 countUnexpiredTokens 操作），过期事件 优先于 其他操作。

 

示例 1：


输入：
["AuthenticationManager", "renew", "generate", "countUnexpiredTokens", "generate", "renew", "renew", "countUnexpiredTokens"]
[[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]
输出：
[null, null, null, 1, null, null, null, 0]

解释：
AuthenticationManager authenticationManager = new AuthenticationManager(5); // 构造 AuthenticationManager ，设置 timeToLive = 5 秒。
authenticationManager.renew("aaa", 1); // 时刻 1 时，没有验证码的 tokenId 为 "aaa" ，没有验证码被更新。
authenticationManager.generate("aaa", 2); // 时刻 2 时，生成一个 tokenId 为 "aaa" 的新验证码。
authenticationManager.countUnexpiredTokens(6); // 时刻 6 时，只有 tokenId 为 "aaa" 的验证码未过期，所以返回 1 。
authenticationManager.generate("bbb", 7); // 时刻 7 时，生成一个 tokenId 为 "bbb" 的新验证码。
authenticationManager.renew("aaa", 8); // tokenId 为 "aaa" 的验证码在时刻 7 过期，且 8 >= 7 ，所以时刻 8 的renew 操作被忽略，没有验证码被更新。
authenticationManager.renew("bbb", 10); // tokenId 为 "bbb" 的验证码在时刻 10 没有过期，所以 renew 操作会执行，该 token 将在时刻 15 过期。
authenticationManager.countUnexpiredTokens(15); // tokenId 为 "bbb" 的验证码在时刻 15 过期，tokenId 为 "aaa" 的验证码在时刻 7 过期，所有验证码均已过期，所以返回 0 。
 

提示：

1 <= timeToLive <= 108
1 <= currentTime <= 108
1 <= tokenId.length <= 5
tokenId 只包含小写英文字母。
所有 generate 函数的调用都会包含独一无二的 tokenId 值。
所有函数调用中，currentTime 的值 严格递增 。
所有函数的调用次数总共不超过 2000 次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-authentication-manager
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.id_time = dict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.id_time[tokenId] = currentTime+self.timeToLive
        # print('generate',tokenId,self.id_time[tokenId])

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.id_time:
            if self.id_time[tokenId]>currentTime:
                self.id_time[tokenId] = currentTime+self.timeToLive
                # print('renew',tokenId,self.id_time[tokenId])
            else:
                self.id_time.pop(tokenId)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.id_time = dict((id,time) for id,time in self.id_time.items() if time>currentTime)
        # print(currentTime,self.id_time,len(self.id_time))
        return len(self.id_time)
        # return len([id,time for id,time in self.id_time.items() if time>currentTime])


def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.getResult(*data)

def test_obj(data_test):
    result = [None]
    obj = AuthenticationManager(*data_test[1][0])
    for fun,data in zip(data_test[0][1::],data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
    return result

if __name__ == '__main__':
    datas = [
        # [["AuthenticationManager","renew","generate","countUnexpiredTokens","generate","renew","renew","countUnexpiredTokens"],[[5],["aaa",1],["aaa",2],[6],["bbb",7],["aaa",8],["bbb",10],[15]]],
        # [["AuthenticationManager","countUnexpiredTokens","renew","generate","renew","countUnexpiredTokens","renew","generate","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens"],[[28],[2],["xokiw",6],["ofn",7],["dses",15],[17],["ofzu",19],["dses",20],[23],[27],[30]]],
        [["AuthenticationManager","renew","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","generate","generate","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","renew","countUnexpiredTokens","countUnexpiredTokens","renew","countUnexpiredTokens","generate","renew","countUnexpiredTokens","countUnexpiredTokens","renew","renew","renew","generate","renew","generate","countUnexpiredTokens","countUnexpiredTokens","generate","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","renew","generate","generate","generate","countUnexpiredTokens","renew","generate","countUnexpiredTokens","countUnexpiredTokens","generate","generate","generate","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","renew","renew","renew","countUnexpiredTokens","countUnexpiredTokens"],[[104],["ox",50],[73],[87],[93],["yyeu",104],["r",131],[167],[172],[191],[206],[232],["r",235],[239],[257],["vi",268],[292],["vi",296],["yu",303],[326],[339],["aimzm",343],["umdzy",346],["qyf",347],["mfne",353],["nn",357],["hz",359],[422],[434],["pel",473],[494],[498],[508],[524],["pt",552],["vbaa",568],["gt",592],["zxdv",611],[618],["fbp",619],["giih",622],[623],[629],["chmi",659],["doohl",671],["svxbv",715],[722],[749],[754],[771],[794],["pel",865],["i",919],["aqa",962],[976],[978]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test_obj(data_test))
        print(f'use time:{time.time() - t0}s')
