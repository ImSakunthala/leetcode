"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.An Anagram is a word or phrase
formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagram -> a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from
        # rasp, in other words presence of permutation of one string in another string.

        if len(s) != len(t):
            return False
        # create dictionary for base string
        count_s = dict(Counter(s))

        # check char in another present in base string dictionary.
        for char in t:
            # False -> if char is not present or count of the char is equal to zero -> not anagram of base string
            if char not in count_s or count_s[char] == 0:
                return False
            # Decrease the count of the char in base string
            else:
                count_s[char] -= 1
        # True -> if all character count in another string makes all character in base string to zero.
        return True


solution = Solution()
assert solution.isAnagram(s="ab", t="a") == False
assert solution.isAnagram(s="anagram", t="nagaram") == True
assert solution.isAnagram(s="rat", t="car") == False
