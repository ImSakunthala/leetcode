"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]



Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from typing import List


def sum_of_two(nums: List[int], target: int) -> List[int]:
    result = []

    for first_idx, first_element in enumerate(nums):
        start_idx = first_idx+1
        for second_idx, second_element in enumerate(nums[start_idx:]):
            if first_element+second_element == target:
                result.append(first_idx)
                result.append(start_idx + second_idx)
                break
        if len(result) > 0:
            break
    return result


print(sum_of_two([11, 15, 7, 2], 4))
