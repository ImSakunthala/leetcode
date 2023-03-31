"""
Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i,
j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.

Example 1:

Input: nums = ["777","7","77","77"], target = "7777"
Output: 4
Explanation: Valid pairs are:
- (0, 1): "777" + "7"
- (1, 0): "7" + "777"
- (2, 3): "77" + "77"
- (3, 2): "77" + "77"

Example 2:

Input: nums = ["123","4","12","34"], target = "1234"
Output: 2
Explanation: Valid pairs are:
- (0, 1): "123" + "4"
- (2, 3): "12" + "34"
Example 3:

Input: nums = ["1","1","1"], target = "11"
Output: 6
Explanation: Valid pairs are:
- (0, 1): "1" + "1"
- (1, 0): "1" + "1"
- (0, 2): "1" + "1"
- (2, 0): "1" + "1"
- (1, 2): "1" + "1"
- (2, 1): "1" + "1"


Constraints:

2 <= nums.length <= 100
1 <= nums[i].length <= 100
2 <= target.length <= 100
nums[i] and target consist of digits.
nums[i] and target do not have leading zeros.
"""
from typing import List
from itertools import permutations
from collections import Counter


class Solution:
    def pairs(self, nums: List[str]) -> list[str]:
        # TIL: python inbuilt module itertools -> permutations -> return tuple of specified length if length not
        # specified it returns all possible ways of permutations in array
        return list(permutations(nums, 2))

    def numOfPairs(self, nums: List[str], target: str) -> int:
        # to create a list of sub-arrays of length two with all indices
        pairs_subarray = self.pairs(nums)

        # Count -> to keep track of strings equal to target string
        count = 0

        # loop through the pairs and concatenation them to check if it is equal to target string
        for (str1, str2) in pairs_subarray:

            # if it is equal to target string them increase the count by one
            if str1 + str2 == target:
                count += 1

        # Return count of target string in given arrays
        return count

    def num_of_pairs(self, nums: List[str], target: str) -> int:

        # create dictionary for frequency of strings in the given array
        frequency = Counter(nums)

        # Count -> to keep track of strings equal to target string
        count = 0

        # iterate through the given array
        for str1 in nums:

            # check if string 1 is starting character of the given target string
            if target.startswith(str1):

                # if true -> then string 2 should be of remaining part of target array [Note: use slicing]
                str2 = target[len(str1):]

                # check if string 2 in frequency then -> True add the frequency(value) of string 2  to count
                if str2 in frequency:
                    count += frequency[str2]

                    # string 2 == string 1 then decrease count
                    if str2 == str1:
                        count -= 1

        return count


solution = Solution()
assert 6 == solution.num_of_pairs(nums=["1", "1", "1"], target="11")
assert 4 == solution.num_of_pairs(nums=["777", "7", "77", "77"], target="7777")
assert 2 == solution.num_of_pairs(nums=["123", "4", "12", "34"], target="1234")
