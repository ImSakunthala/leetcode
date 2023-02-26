"""
You are given a positive integer n, you can do the following operation any number of times:

Add or subtract a power of 2 from n.
Return the minimum number of operations to make n equal to 0.

A number x is power of 2 if x == 2i where i >= 0.



Example 1:

Input: n = 39
Output: 3
Explanation: We can do the following operations:
- Add 20 = 1 to n, so now n = 40.
- Subtract 23 = 8 from n, so now n = 32.
- Subtract 25 = 32 from n, so now n = 0.
It can be shown that 3 is the minimum number of operations we need to make n equal to 0.
Example 2:

Input: n = 54
Output: 3
Explanation: We can do the following operations:
- Add 21 = 2 to n, so now n = 56.
- Add 23 = 8 to n, so now n = 64.
- Subtract 26 = 64 from n, so now n = 0.
So the minimum number of operations is 3.


Constraints:

1 <= n <= 10^5
"""


class Solution:
    def check_num_range(self, n: int, range_list: list) -> list:
        for index, num in enumerate(range_list):
            smaller = range_list[index]
            greater = range_list[index + 1] if range_list[index + 1] in range_list else 0
            if smaller <= n <= greater:
                num_boundary = [smaller, greater]
                return num_boundary

    def nearest_power(self, n:int, num_boundary: list) -> int:
        return num_boundary[0] if n - num_boundary[0] < num_boundary[1] - n else num_boundary[1]

    def minOperations(self, n: int) -> int:
        count = 0
        range_list = [2 ** x for x in range(0, 18)]  # since 1 <= n <= 10^5
        while n != 0:
            check_num_range = self.check_num_range(n, range_list)
            nearest_power = self.nearest_power(n, check_num_range)
            if n < nearest_power:
                n = nearest_power - n
            else:
                n = n - nearest_power
            count += 1

        return count


solution = Solution()
assert 7 == solution.minOperations(n=97123)
assert 3 == solution.minOperations(n=39)
assert 3 == solution.minOperations(n=54)
assert 3 == solution.minOperations(n=81)
assert 3 == solution.minOperations(n=27)
assert 2 == solution.minOperations(n=124)
assert 2 == solution.minOperations(n=56)
