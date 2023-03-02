"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.



Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6


Constraints:

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000
"""
from typing import List
from itertools import permutations
import math


class Solution:
    def sub_arrays_of_3(self, nums: List[int]) -> List[int]:
        result = list(permutations(nums, 3))
        return result

    def maximumProduct(self, nums: List[int]) -> int:
        sub_arrays = self.sub_arrays_of_3(nums)
        result = []

        for array in sub_arrays:
            result.append(math.prod(array))
        return max(result)


solution = Solution()
assert solution.maximumProduct(nums=[-100, -98, -1, 2, 3, 4]) == 39200
assert solution.maximumProduct(nums=[1, 2, 3]) == 6
assert solution.maximumProduct(nums=[1, 2, 3, 4]) == 24
assert solution.maximumProduct(nums=[-1, -2, -3]) == -6
