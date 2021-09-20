# -*- coding: utf-8 -*-
# @File  : leet_12.py
# @Author: FanyFull
# @Date  : 2021/9/20

class Solution:
    def intToRoman(self, num: int) -> str:
        number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        s = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ""

        for i in range(0, len(number)):
            #
            while (num >= number[i]):
                res += s[i]
                num -= number[i]

            if num <= 0:
                break

        return res

if __name__ == '__main__':
    solution = Solution()
    input = 1994
    output = solution.intToRoman(input)
    print(output)