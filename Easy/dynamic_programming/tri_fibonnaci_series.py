"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537


Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""


class Solution:
    tribonacci_dict = {}

    def tribonacci(self, n: int) -> int:
        # using recursive method
        if n == 0:
            return 0
        elif 1 <= n <= 2:
            return 1
        else:
            return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        # this program will give time complexity of O(3^n)

    def tribonacci_memo(self, n: int) -> int:
        # using recursive method
        if n == 0:
            return 0
        elif 0 < n <= 2:
            return 1
        elif n in self.tribonacci_dict.keys():
            return self.tribonacci_dict[n]
        else:
            tri_value = self.tribonacci_memo(n - 1) + self.tribonacci_memo(n - 2) + self.tribonacci_memo(n - 3)
            self.tribonacci_dict[n] = tri_value
            return tri_value

    def tri_fibonacci(self, n: int) -> int:

        # using iteration method
        t0, t1, t2 = 0, 1, 1

        for n in range(3, n + 1):
            temp = t0 + t1 + t2
            t0, t1, t2 = t1, t2, temp

        if n == 0:
            return 0
        else:
            return t2

    def Tribonacci_series(self, n: int) -> int:

        value_dict = {0: 0, 1: 1, 2: 1}
        # initialize dictionary values

        for num in range(3, n + 1):
            a, b, c = value_dict[num - 1], value_dict[num - 2], value_dict[num - 3]
            value = a + b + c
            value_dict[num] = value

        return value_dict[n]


solution = Solution()
print(solution.tribonacci_memo(n=5))
print(solution.Tribonacci_series(n=2))
