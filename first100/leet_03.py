# -*- coding: utf-8 -*-
# @File  : leet_03.py
# @Author: FanyFull
# @Date  : 2021/7/10

# 暴力解法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end):
            chars = [0] * 128
            for i in range(start, end + 1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True

        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res

# 滑动窗口
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        left = right = 0
        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1
            # chars[r] > 1 表明从 left 到 right 之间出现重复的字符了
            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res

# 滑动窗口优化
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        mp = {}
        i = 0
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            ans = max(j - i + 1, ans)
            mp[s[j]] = j + 1
        return ans

class Solution3_2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128
        left = right = 0
        res = 0
        while right < len(s):
            r = s[right]
            index = chars[ord(r)]
            # 出现重复的字符了
            if index != None and index >= left and index < right:
                left = index + 1
            res = max(res, right - left + 1)
            chars[ord(r)] = right
            right += 1
        return res

if __name__ == '__main__':
    solution = Solution3_2()
    s = 'abcdeabcd'
    print(solution.lengthOfLongestSubstring(s))

