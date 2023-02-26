"""
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def binary_int(self, a: str) -> int:
        convert = [int(element) for element in a]
        result = 0
        for index, element in enumerate(convert[::-1]):
            num = element * (2 ** index)
            result += num
        return result

    def int_binary(self, number: int) -> str:
        result = ""
        if number == 0:
            return '0'
        while number:
            result += str(number & 1)
            number = number >> 1

        return result[::-1]

    def addBinary(self, a: str, b: str) -> str:
        a = self.binary_int(a)
        b = self.binary_int(b)
        result = a + b
        return self.int_binary(result)


solution = Solution()
print('11 ->', solution.int_binary(number=4))
print("100 ->", solution.addBinary(a="11", b="1"))
print("10101 ->", solution.addBinary(a="1010", b="1011"))
