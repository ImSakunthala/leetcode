"""
Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.



Example 1:

Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
Example 2:

Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1, 5.
"""


class Solution:
    def commonFactors(self, a: int, b: int) -> int:

        factors_of_a, factors_of_b = [], []

        for num in range(1, a + 1):
            if a % num == 0:
                factors_of_a.append(num)

        for num in range(1, b + 1):
            if b % num == 0:
                factors_of_b.append(num)

        common_factors = []
        for factor_a in factors_of_a:
            if factor_a in factors_of_b:
                common_factors.append(factor_a)

        return len(common_factors)


solution = Solution()
assert 4 == solution.commonFactors(a=12, b=6)
assert 2 == solution.commonFactors(a=25, b=30)
