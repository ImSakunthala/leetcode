"""
Given an integer array nums of length n, you want to create an array answer of length 2n where ans[i] == nums[i]
 and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, answer is the concatenation of two nums arrays.

Return the array ans.

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array answer is formed as follows:
- answer = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- answer = [1,2,1,1,2,1]
Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array answer is formed as follows:
- answer = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- answer = [1,3,2,1,1,3,2,1]

Constraints:

n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000
"""


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        copy_input = nums

        result = nums + copy_input

        return result

    def get_Concatenation(self, nums: list[int]) -> list[int]:

        result = []

        for num in nums:
            result.append(num)

        for item in nums:
            result.append(item)

        return result

    def Concatenation_of_list(self, nums: list[int]) -> list[int]:

        result = []
        for i in (nums, nums):
            for j in i:
                result.append(j)

        return result

    def Concatenation_list(self, nums: list[int]) -> list[int]:

        nums.extend(nums)

        return nums

    def list_Concatenation(self, nums: list[int]) -> list[int]:

        result = [*nums, *nums]

        return result

    def listConcatenation(self, nums: list[int]) -> list[int]:

        import itertools

        result = list(itertools.chain(nums, nums))

        return result


solution = Solution()
print('[1, 3, 2, 1, 1, 3, 2, 1] ->', solution.listConcatenation(nums=[1, 3, 2, 1]))
