"""
Given an integer num, return a string of its base 7 representation.



Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"


Constraints:

-107 <= num <= 107
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        base_7 = ''

        if num == 0:
            return '0'

        is_negative = num < 0

        if is_negative:
            num = -num

        while num > 0:
            base_7 += str(num % 7)
            num = num // 7

        return '-' + base_7[::-1] if is_negative else base_7[::-1]


solution = Solution()
assert 160 == solution.convertToBase7(num=91)
assert 202 == solution.convertToBase7(num=100)
assert -10 == solution.convertToBase7(num=-7)
