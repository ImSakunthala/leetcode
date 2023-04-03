"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true


Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # defining two empty dictionaries to store the key and value of both the strings

        string_map1 = {}
        string_map2 = {}

        # to check whether both string is of same length if not return False directly no need of proceeding further.

        if len(s) == len(t):

            # getting the characters from both the string
            for ch_1, ch_2 in zip(s, t):

                # check whether mapping of the string exists in string_map of both the strings.
                # And check mapping of already existing character not in another string
                # if both condition Fail then return False
                # All the above condition to avoid over-riding of existing dictionary key and value

                if (ch_1 in string_map1 and string_map1[ch_1] != ch_2) or (ch_2 in string_map2 and string_map2[ch_2] != ch_1):
                    return False

                # if it doesn't exist in mapping then add to the dictionary and return True,
                # after completion of all the characters in both strings.

                string_map1[ch_1] = ch_2
                string_map2[ch_2] = ch_1

            return True

        else:
            return False


solution = Solution()
print(solution.isIsomorphic('aaabbbba','bbbaaaba'))