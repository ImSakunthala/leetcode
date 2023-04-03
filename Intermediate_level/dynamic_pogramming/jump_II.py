"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at
nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and i + j < n Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated
such that you can reach nums[n - 1].

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        length_of_nums = len(nums)

        if length_of_nums <= 1:
            return 0
        else:
            # maximum jumps -> represent the nums[i].
            # jumps -> to know how many times we jumped to reach length of nums -1.
            # end -> to check whether we reached length of nums - 1.
            maximum_jumps, jumps, end = 0, 0, 0

            for i in range(length_of_nums - 1):
                # update maximum_jumps with index and nums[index].
                maximum_jumps = max(maximum_jumps, i + nums[i])

                if i == end:
                    end = maximum_jumps
                    jumps += 1

            return jumps


solution = Solution()
assert 0 == solution.jump(nums=[1])
assert 0 == solution.jump(nums=[])
assert 2 == solution.jump(nums=[2, 3, 1, 1, 4])
assert 2 == solution.jump(nums=[2, 3, 0, 1, 4])
