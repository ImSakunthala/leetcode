"""
Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.



Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.
Example 3:

Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.


Constraints:

1 <= nums.length <= 2000
0 <= nums[i] <= 105
"""
from typing import List
from collections import Counter


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        result, frequency = -1, 0

        for num in num_count:
            if num % 2 == 0:
                if num_count[num] > frequency:
                    frequency = num_count[num]
                    result = num
                elif num_count[num] == frequency and num < result:
                    result = num
        return result


solution = Solution()
assert solution.mostFrequentEven(
    nums=[4287, 799, 8103, 3526, 8396, 7060, 8287, 4214, 4093, 6763, 651, 4907, 8350, 4866, 5114, 5245,
          3198, 6644, 3620, 1586, 3068, 2769, 9506, 2319, 588, 5055, 730, 6968, 4814, 144, 5180, 8798,
          8783, 3319, 7765, 3254, 7164, 5462, 8085, 5481, 8363, 3135, 2910, 583, 3751, 3044, 8734, 4075,
          5489, 7866, 3404, 9532, 3751, 571, 7460, 4934, 9346, 4076, 1505, 9576, 9406, 3342, 8090, 5979,
          3140, 4453, 4779, 9324, 2945, 7279, 6809, 9619, 6958, 9881, 8308, 9246, 2529, 3727, 1241, 7230,
          4536, 9852, 1667, 1688, 1320, 6400, 6359, 6140, 904, 6287, 6499, 9256, 7666, 4083, 2927, 3165,
          9239, 9433, 1620, 6961, 3115, 8766, 2416, 6653, 9030, 2690, 9165, 6150, 1644, 5925]) == 144
assert solution.mostFrequentEven(nums=[0, 1, 2, 2, 4, 4, 1]) == 2
assert solution.mostFrequentEven(nums=[29, 47, 21, 41, 13, 37, 25, 7]) == -1
assert solution.mostFrequentEven(nums=[4, 4, 4, 9, 2, 4]) == 4
