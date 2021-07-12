# -*- coding: utf-8 -*-
# @File  : leet_08.py
# @Author: FanLu
# @Date  : 2021/7/12

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0 # 索引
        ans = 0 # 结果
        pos_or_neg = 1 # 正还是负
        while i < len(s) and s[i] == ' ':
            i += 1 # 找到第一个非空格的字符
        if i == len(s):
            return 0
        # 确定正负
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            pos_or_neg = -1
            i += 1
        # 当前 i 索引位置上的字符必须是数字才能触发这个 while 循环
        while i < len(s) and s[i] >= '0' and s[i] <= '9':
            ans = ans * 10 + int(s[i])
            i += 1
            if ans > 2 ** 31 - 1:
                if pos_or_neg == 1:
                    return 2 ** 31 - 1
                else:
                    return -2 ** 31
        return ans * pos_or_neg

if __name__ == '__main__':
    solution = Solution()
    s = '   -42'
    s = '4193 with words'
    s = 'words and 987'
    ans = solution.myAtoi(s)
    print(ans)
