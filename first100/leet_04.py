# -*- coding: utf-8 -*-
# @File  : leet_04.py
# @Author: FanyFull
# @Date  : 2021/7/10

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 寻找两个数组中的第 k 个元素
        def find_kth(nums1:List[int], i:int, nums2:List[int], j:int, k:int):
            if i >= len(nums1):
                return nums2[j + k - 1]
            if j >= len(nums2):
                return nums1[i + k - 1]
            if k == 1:
                return min(nums1[i], nums2[j])
            mid_val1 = nums1[i - 1 + k // 2] if i - 1 + k // 2 < len(nums1) else float('inf')
            mid_val2 = nums2[j - 1 + k // 2] if j - 1 + k // 2 < len(nums2) else float('inf')
            if mid_val1 < mid_val2:
                return find_kth(nums1, i + k // 2, nums2, j, k - k // 2)
            else:
                return find_kth(nums1, i, nums2, j + k // 2, k - k // 2)

        m = len(nums1)
        n = len(nums2)
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2
        return (find_kth(nums1, 0, nums2, 0, left) + find_kth(nums1, 0, nums2, 0, right)) / 2

if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 3] # 注意，这里的输入数组都是正序的
    nums2 = [2]
    ans = solution.findMedianSortedArrays(nums1, nums2)
    print(ans)

