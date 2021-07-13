# -*- coding: utf-8 -*-
# @File  : leet_10.py
# @Author: FanLu
# @Date  : 2021/7/13

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def is_match(s: str, p: str) -> bool:
            if p == '':
                return s == ''

            # 判断 s 和 p 的首字母是否匹配，注意要先判断 s 不为空
            head_matched = not (s == '') and (s[0] == p[0] or p[0] == '.')
            if len(p) >= 2 and p[1] == '*':
                return is_match(s, p[2:]) or (head_matched and is_match(s[1:], p))
            elif head_matched:
                return is_match(s[1:], p[1:])
            else:
                return False

        return is_match(s, p)

if __name__ == '__main__':
    solution = Solution()
    s = 'a'
    p = '.*'
    output = solution.isMatch(s, p)
    print(output)
