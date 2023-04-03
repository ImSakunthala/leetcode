Medium/permutation_in_string.py

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
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Base Condition: if length of s1 is greater than s2, then there is no possibility of finding substring
        if len(s1) > len(s2):
            return False

        else:
            # TIL -> itertools -> permutation, this is very effective until you have string of small_length
            # if it exceeds more than 20 it takes more time to evaluate, so another approach is effective.
            base_permutation = [''.join(p) for p in permutations(s1)]

            # sliding window concept for s2 separation based on string_1 length
            pairs = []
            for i in range(len(s2) - len(s1) + 1):
                pairs.append(s2[i:i+len(s1)])

            # True -> if the pair exists in base permutation
            # else -> False
            for pair in pairs:
                if pair in base_permutation:
                    return True
            return False


solution = Solution()
print('True ->', solution.checkInclusion(s1='ab', s2='eidbaoo'))
print('False ->', solution.checkInclusion(s1='ab', s2='eidboaoo'))