"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.



Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true


Constraints:

-231 <= n <= 231 - 1
"""
import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and math.log(n, 4).is_integer()


solution = Solution()
print(solution.isPowerOfFour(n=1))
print(solution.isPowerOfFour(n=-28))
print(solution.isPowerOfFour(n=16))
print(solution.isPowerOfFour(n=6))
