# -*- coding: utf-8 -*-
# @File  : leet_11.py
# @Author: FanLu
# @Date  : 2021/7/15

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 1:
            return -1
        i = 0
        j = len(height) - 1
        ans = 0
        while i < j:
            h = min(height[i], height[j])
            ans = max(ans, h * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    height = [1, 1]
    height = [4, 3, 2, 1, 4]
    height = [1, 2, 1]
    ans = solution.maxArea(height)
    print(ans)
