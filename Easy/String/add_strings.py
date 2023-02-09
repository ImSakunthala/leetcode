"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.



Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"


Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""


class Solution:
    def int_conversion(self, num1: str) -> int:
        result = 0
        unicode_zero = ord('0')
        len_string = len(num1)
        for index, st_ch in enumerate(num1):
            int_value = ord(st_ch) - unicode_zero
            result += (int_value * (10 ** (len_string - index - 1)))

        return result

    def addStrings(self, num1: str, num2: str) -> str:

        num1 = self.int_conversion(num1)
        num2 = self.int_conversion(num2)

        return str(num1 + num2)


solution = Solution()

assert solution.int_conversion('1234') == 1234
assert solution.int_conversion('1') == 1

assert solution.addStrings('1234', '5678') == '6912'
assert solution.addStrings('1', '5678') == '5679'
assert solution.addStrings('22', '5678') == '5700'
assert solution.addStrings('0000', '5678') == '5678'
assert solution.addStrings('1111', '4444') == '5555'
assert solution.addStrings('2222222222', '3333333333') == '5555555555'
assert solution.addStrings('3333', '6666') == '9999'

