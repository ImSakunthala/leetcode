"""
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.



Example 1:

Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.
Example 2:

Input: nums = [7,5,6,8,3]
Output: 1
Explanation:
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.
Example 3:

Input: nums = [3,3]
Output: 3
Explanation:
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.


Constraints:

2 <= nums.length <= 1000
1 <= nums[i] <= 1000
"""

from typing import List
import math


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        return math.gcd(min_num, max_num)

    def find_GCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        factors_min_num = []
        for number in range(1, min_num + 1):
            if (min_num % number) == 0:
                factors_min_num.append(number)

        factors_max_num = []
        for element in range(1, max_num + 1):
            if (max_num % element) == 0:
                factors_max_num.append(element)

        common_factor = []
        for factors in factors_max_num:
            if factors in factors_min_num:
                common_factor.append(factors)

        return max(common_factor)




solution = Solution()
print('2 ->', solution.find_GCD(nums = [2,5,6,9,10]))
print('1 ->', solution.find_GCD(nums = [7,5,6,8,3]))
print('3 ->', solution.find_GCD(nums = [3,3]))