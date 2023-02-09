"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1


Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""
from typing import List


class Solution:
    @staticmethod
    def singleNumber(nums: List[int]) -> int:
        nums.sort()
        print(nums)
        position = 0
        while True:
            if position + 1 < len(nums) and nums[position] == nums[position + 1]:
                position += 2
            else:
                return nums[position]


solution = Solution()
print(solution.singleNumber([1, 2, 3, 2, 1]))
