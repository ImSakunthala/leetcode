"""
Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation:
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
Example 2:

Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
Example 3:

Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # consecutive_zeros -> For each zero, you can calculate the number of zero-filled sub-arrays that end on that
        # index, which is the number of consecutive zeros behind the current element + 1 count_arrays -> Maintain the

        # number of consecutive zeros behind the current element, count the number of zero-filled sub-arrays that end
        # on each index, sum it up to get the answer
        consecutive_zeros, count_arrays = 0, 0

        for num in nums:
            if num != 0:
                consecutive_zeros = 0

            else:
                consecutive_zeros += 1

            count_arrays += consecutive_zeros

        return count_arrays


solution = Solution()
assert 6 == solution.zeroFilledSubarray(nums=[1, 3, 0, 0, 2, 0, 0, 4])
assert 9 == solution.zeroFilledSubarray(nums=[0, 0, 0, 2, 0, 0])
assert 0 == solution.zeroFilledSubarray(nums=[2, 10, 2019])
assert 4 == solution.zeroFilledSubarray(nums=[0, 0, 2, 0])
assert 153 == solution.zeroFilledSubarray(nums=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
