"""A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements
is the same.
Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression.
Otherwise, return false.

Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.


Constraints:

2 <= arr.length <= 1000
-106 <= arr[i] <= 106
"""
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sorted_array = sorted(arr)
        diff = sorted_array[-1] - sorted_array[-2]
        difference = [0] * (len(arr) - 1)

        for index, num1 in enumerate(sorted_array[:-1]):
            if sorted_array[index + 1] - num1 == diff:
                difference[index] = True
            else:
                return False
        return True


solution = Solution()
assert True == solution.canMakeArithmeticProgression(arr=[3, 5, 1])
assert False == solution.canMakeArithmeticProgression(arr=[1, 2, 4])
