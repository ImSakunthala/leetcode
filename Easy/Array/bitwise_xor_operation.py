"""
You are given an integer n and an integer start.

Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.

Example 1:

Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.

Example 2:

Input: n = 4, start = 3
Output: 8
Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.


Constraints:

1 <= n <= 1000
0 <= start <= 1000
n == nums.length
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        resultant_array = [start]

        while len(resultant_array) != n:
            last_element = resultant_array[-1]
            resultant_array.append(last_element + 2)

        for num in resultant_array:
            result = result ^ num

        return result


solution = Solution()
print('8 ->', solution.xorOperation(n=5, start=0))
print('8 ->', solution.xorOperation(n=4, start=3))
