# -*- coding: utf-8 -*-
# @File  : draft07.py
# @Author: FanLu
# @Date  : 2021/7/11

from typing import List

def find_kth(nums1: List[int], i: int, nums2: List[int], j: int, k: int):
    if i >= len(nums1):
        return nums2[j + k - 1]
    if j >= len(nums2):
        return nums1[i + k - 1]
    if k == 1:
        return min(nums1[i], nums2[j])
    mid_val1 = nums1[i + k // 2 - 1] if i + k // 2 - 1 < len(nums1) else float('inf')
    mid_val2 = nums2[j + k // 2 - 1] if j + k // 2 - 1 < len(nums2) else float('inf')
    if mid_val1 < mid_val2:
        return find_kth(nums1, i + k // 2, nums2, j, k - k // 2)
    else:
        return find_kth(nums1, i, nums2, j + k // 2, k - k // 2)

# 注意，这两个数组必须是正序的
nums1 = [1, 2, 3, 4, 5]
nums2 = [2]
print(find_kth(nums1, 0, nums2, 0, 3))
