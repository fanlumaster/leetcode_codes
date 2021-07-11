# -*- coding: utf-8 -*-
# @File  : leet_06.py
# @Author: FanyFull
# @Date  : 2021/7/11

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        row_strs = []
        for i in range(numRows):
            row_strs.append('')
        row = 0
        flag = -1
        for i in range(len(s)):
            row_strs[row] += s[i]
            if row == 0 or row == numRows - 1:
                flag = -flag
            row += flag
        ans = ''
        for each in row_strs:
            ans += each
        return ans

if __name__ == '__main__':
    solution = Solution()
    s = 'AB'
    numRows = 1
    ans = solution.convert(s, numRows)
    print(ans)
