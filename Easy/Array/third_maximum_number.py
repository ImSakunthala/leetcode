"""
Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.


Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""


class Solution:
    def thirdMax(self, nums: list[int]) -> int:

        new_input = list(set(nums))
        new_input.sort()

        return new_input[-3] if len(new_input) >= 3 else max(new_input)


solution = Solution()
print(solution.thirdMax(nums=[2, 2, 1, 3]))
print(solution.thirdMax(nums=[1, 2, 3, 4, 5, 6]))
print(solution.thirdMax(nums=[5, 5, 10, 12, -1]))
print(solution.thirdMax(nums=[-1, -2, -3, -5, -6]))
print(solution.thirdMax(nums=[1, -2, -1, 3, 6, 7, 9]))
print(solution.thirdMax(nums=[-4, 4]))

