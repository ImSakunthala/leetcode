"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""
from itertools import permutations


class Solution:
    def permutation(self, string: str) -> list:
        string_permutation = [''.join(char for char in permutations(string))]
        return [string_permutation]




    # def checkInclusion(self, s1: str, s2: str) -> bool:


solution = Solution()
print(solution.permutation(string='ab'))
# print('True ->', solution.checkInclusion(s1 = "ab", s2 = "eidbaooo"))
# print('False ->', solution.checkInclusion(s1 = "ab", s2 = "eidboaoo"))
