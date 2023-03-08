"""Given an integer num, return a string representing its hexadecimal representation. For negative integers,
two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the
answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.


Example 1:

Input: num = 26
Output: "1a"

Example 2:

Input: num = -1
Output: "ffffffff"
"""


class Solution:
    def toHex(self, num: int) -> str:

        conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                            5: '5', 6: '6', 7: '7',
                            8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c',
                            13: 'd', 14: 'e', 15: 'f'}

        hexadecimal = ''

        while num > 0:
            remainder = num % 16
            hexadecimal = conversion_table[remainder] + hexadecimal
            num = num // 16

        return hexadecimal


solution = Solution()
print(solution.toHex(num=26))

