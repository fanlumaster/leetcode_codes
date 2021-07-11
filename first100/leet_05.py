# -*- coding: utf-8 -*-
# @File  : leet_05.py
# @Author: FanLu
# @Date  : 2021/7/11

from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find_longest(s: str, low: int, range_list: List[int]) -> int:
            high = low
            while high < len(s) - 1 and s[high + 1] == s[low]:
                high += 1
            # 定位中间部分的最后一个字符
            ans = high
            # 从中间向左右两边扩散
            while low > 0 and high < len(s) - 1 and s[low - 1] == s[high + 1]:
                low -= 1
                high += 1
            if high - low > range_list[1] - range_list[0]:
                range_list[0] = low
                range_list[1] = high
            return ans
        if s == None and len(s) == 0:
            return ''
        # 保存起止位置
        range_list = [0] * 2
        for i in range(0, len(s)):
            i = find_longest(s, i, range_list)
            continue
        return s[range_list[0]:range_list[1] + 1]

if __name__ == '__main__':
    solution = Solution()
    s = 'abcdcbaa'
    ans = solution.longestPalindrome(s)
    print(ans)