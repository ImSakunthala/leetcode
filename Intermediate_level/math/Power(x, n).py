"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-10^4 <= xn <= 10^4
"""


class Solution:
    def basecondition(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0

        result = self.myPow(x, n // 2)
        result = result * result

        if n % 2 != 0:
            return result * x
        else:
            return result

    def myPow(self, x: float, n: int) -> float:
        result = self.basecondition(x, abs(n))

        if n >= 0:
            return result
        else:
            return 1 / result

    def myPow_1(self, x: float, n: int) -> float:
        return x ** n


solution = Solution()
assert 0.0009765625 == solution.myPow(x=2.00000, n=-10)
assert 1024.00 == solution.myPow(x=2.00000, n=10)
