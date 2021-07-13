# -*- coding: utf-8 -*-
# @File  : draft10.py
# @Author: FanLu
# @Date  : 2021/7/13

import re

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s1 = re.compile(p).findall(s)
        if s1 == []:
            return False;
        if s1[0] == s:
            return True;
        else:
            return False;
if __name__ == '__main__':
    solution = Solution()
    s = 'a'
    p = '.*'
    output = solution.isMatch(s, p)
    print(output)