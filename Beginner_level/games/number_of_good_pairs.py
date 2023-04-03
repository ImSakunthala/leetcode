"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0


Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        result = 0
        for index_i, value_i in enumerate(nums):
            # create sub_list from nums with index_i + 1, thus index_i < index_j
            for index_j, value_j in enumerate(nums[index_i + 1:]):
                if value_i == value_j:
                    result += 1

        return result

    def numidenticalpairs_while(self, nums: list[int]) -> int:
        result = 0
        index_i = 0
        length_of_nums = len(nums)
        while index_i < length_of_nums - 1:
            index_j = index_i + 1
            while index_j < length_of_nums:
                if nums[index_i] == nums[index_j] and index_i < index_j:
                    result += 1
                index_j += 1
            index_i += 1

        return result


solution = Solution()
print('4 - >', solution.numidenticalpairs_while(nums=[1, 2, 3, 1, 1, 3]))
print('6 ->', solution.numidenticalpairs_while(nums=[1, 1, 1, 1]))
print('0 ->', solution.numidenticalpairs_while(nums=[1, 2, 3]))
