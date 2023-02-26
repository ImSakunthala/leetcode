"""Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] -
nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.


Example 1:

Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
Example 2:

Input: nums = [1,3], k = 3
Output: 0
Explanation: There are no pairs with an absolute difference of 3.
Example 3:

Input: nums = [3,2,1,5,4], k = 2
Output: 3
Explanation: The pairs with an absolute difference of 2 are:
- [3,2,1,5,4]
- [3,2,1,5,4]
- [3,2,1,5,4]


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
1 <= k <= 99
"""
from collections import defaultdict
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0

        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums):
                if index1 < index2:
                    if abs(num1 - num2) == k:
                        count += 1
        return count

    def count_KDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        counter = 0
        for num in nums:
            tmp, tmp2 = num - k, num + k
            if tmp in seen:
                counter += seen[tmp]
            if tmp2 in seen:
                counter += seen[tmp2]

            seen[num] += 1

        return counter


solution = Solution()
assert 4 == solution.count_KDifference(nums=[1, 2, 2, 1], k=1)
assert 0 == solution.countKDifference(nums=[1, 3], k=3)
assert 3 == solution.countKDifference(nums=[3, 2, 1, 5, 4], k=2)
