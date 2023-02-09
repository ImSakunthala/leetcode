"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Constraints:
-231 <= x <= 231 - 1
"""
class Solution:
    def reverse_number(self, num: int) -> int:
        x = abs(num)
        result = 0
        while x != 0:
            x, digit = divmod(x, 10)
            result = result * 10 + digit
        return result if num > 0 else -result


solution = Solution()
assert 321 == solution.reverse_number(123)
assert -8463847412 == solution.reverse_number(-2147483648)