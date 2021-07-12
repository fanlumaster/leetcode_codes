# -*- coding: utf-8 -*-
# @File  : leet_07.py
# @Author: FanLu
# @Date  : 2021/7/12

class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        flag = 0 if x > 0 else 1
        x = abs(x)
        while x != 0:
            ans = ans * 10 + x % 10
            x = x // 10
        if flag:
            ans = -ans

        if x < -2 ** 31 or x > 2 ** 31 - 1 or ans < -2 ** 31 or ans > 2 ** 31 - 1:
            return 0
        return ans

# 这个方法要快一点，有时候会快很多（看 LeetCode 心情）
class Solution2:
    def reverse(self, x: int) -> int:
        if x >= 2 ** 31 - 1 or x <= -2 ** 31:
            return 0
        else:
            strg = str(x)
            if x >= 0:
                ans = strg[::-1]
            else:
                temp = strg[1:]
                temp2 = temp[::-1]
                ans = "-" + temp2
            if int(ans) >= 2 ** 31 - 1 or int(ans) <= -2 ** 31:
                return 0
            else:
                return int(ans)


if __name__ == '__main__':
    solution = Solution()
    x = 1534236469
    ans = solution.reverse(x)
    print(ans)
    print(-123 % 10)
