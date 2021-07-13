# -*- coding: utf-8 -*-
# @File  : leet_09.py
# @Author: FanLu
# @Date  : 2021/7/13

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ans = str(x)
        ans_reverse = ans[::-1]
        if ans_reverse == ans:
            return True
        return False

if __name__ == '__main__':
    solution = Solution()
    input = 121
    input = -121
    output = solution.isPalindrome(input)
    print(output)