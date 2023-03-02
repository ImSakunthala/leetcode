"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.



Example 1:

Input: nums = [5,2,3,1] Output: [1,2,3,5] Explanation: After sorting the array, the positions of some numbers are not
changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.


Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        if len(nums) > 1:
            # Split the array into two halves
            mid = len(nums) // 2
            left_half = nums[:mid]
            right_half = nums[mid:]

            # Recursively sort each half
            self.sortArray(left_half)
            self.sortArray(right_half)

            # Merge the two sorted halves
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    nums[k] = left_half[i]
                    i += 1
                else:
                    nums[k] = right_half[j]
                    j += 1
                k += 1

            # Copy any remaining elements from the left half
            while i < len(left_half):
                nums[k] = left_half[i]
                i += 1
                k += 1

            # Copy any remaining elements from the right half
            while j < len(right_half):
                nums[k] = right_half[j]
                j += 1
                k += 1

            return nums


solution = Solution()
assert solution.sortArray(nums=[5, 2, 3, 1]) == [1, 2, 3, 5]
assert solution.sortArray(nums=[5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
