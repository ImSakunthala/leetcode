"""
Given an array of positive integers arr, return the sum of all possible odd-length sub arrays of arr.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length sub arrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 sub arrays of odd length, [1] and [2]. Their sum is 3.
Example 3:

Input: arr = [10,11,12]
Output: 66


Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 1000
"""
from typing import List


class Solution:
    def sub_arrays(self, arr: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(arr)+1):
            for j in range(i):
                result.append(arr[j:i])
        return result

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sub_arrays = self.sub_arrays(arr)
        result = 0
        for array in sub_arrays:
            if len(array) % 2 != 0:
                result += sum(array)
        return result


solution = Solution()
print(solution.sumOddLengthSubarrays(arr=[1, 4, 2, 5, 3]))
