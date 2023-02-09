"""
Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.

An integer m is a divisor of n if there exists an integer k such that n = k * m.



Example 1:

Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.
Example 2:

Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.


Constraints:

1 <= n <= 104
"""


class Solution:
    def isThree(self, n: int) -> bool:
        factors_of_n = []

        for num in range(1, n+1):
            if n % num == 0:
                factors_of_n.append(num)

        return True if len(factors_of_n) == 3 else False


solution = Solution()
print(solution.isThree(n=2))
print(solution.isThree(n=4))
print(solution.isThree(n=6))

