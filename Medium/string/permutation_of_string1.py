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


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # base Condition: if length of s1 is greater than s2, there is no substring
        # so return False
        if len(s1) > len(s2):
            return False

        # create zero map for 26 characters
        string1_map = [0] * 26
        string2_map = [0] * 26

        # map them using ASCII code
        for i in range(len(s1)):
            string1_map[ord(s1[i]) - ord('a')] += 1
            string2_map[ord(s2[i]) - ord('a')] += 1

        # to iterate through the length of s2 but based on the length of s1
        for i in range(len(s2) - len(s1)):

            # if both the map are same return True
            if string1_map == string2_map: return True

            # if not then delete the mapping of first character
            string2_map[ord(s2[i]) - ord('a')] -= 1

            # then, jump to character in s2 based on length of s1,
            # we don,t need mapping of very next character, because it is already done in first for loop
            string2_map[ord(s2[i + len(s1)]) - ord('a')] += 1

        return True if string1_map == string2_map else False


solution = Solution()
print('True ->', solution.checkInclusion(s1='ab', s2='eidbaoo'))
print('False ->', solution.checkInclusion(s1='ab', s2='eidboaoo'))
