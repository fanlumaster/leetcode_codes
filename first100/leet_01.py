# -*- coding: utf-8 -*-
# @File  : leet_01.py
# @Author: FanLu
# @Date  : 2021/7/9

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(0, len(nums)):
            dic[nums[i]] = i
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in dic.keys() and dic[complement] != i:
                return [i, dic[complement]]

class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in dic.keys():
                return [dic[complement], i]
            dic[nums[i]] = i

if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    res = solution.twoSum(nums, target)
    print(res)

