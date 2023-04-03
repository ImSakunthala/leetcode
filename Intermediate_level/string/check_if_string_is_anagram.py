"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""
from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Anagram -> a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from
        # rasp, in other words presence of permutation of one string in another string.

        # Create an empty array to add index at which we find anagram of another string.
        anagram_index = []

        # Check up to which index of s we have to iterate.
        length_of_s, length_of_p = len(s), len(p)

        # when length of s is greater than length of p we have to avoid negative indexing, so we use absolute.
        index_to_iterate = abs(length_of_s - length_of_p)

        # create dictionary for p with counter to know the occurrence.
        count_p = dict(Counter(p))

        # initialize position of starting index
        position = 0

        # since position starts from zero
        while position != index_to_iterate + 1:
            # create a dictionary of s up to the length of p
            count_s = Counter(s[position:(position + length_of_p)])
            # if both the dictionary are same, then append the index to result, clear dictionary and increase index 1.
            if count_s == count_p:
                anagram_index.append(position)
                count_s.clear()
            # else clear dictionary and increase index 1
            else:
                count_s.clear()
            position += 1

        return anagram_index


solution = Solution()
assert [] == solution.findAnagrams(s="aaaaaaaaaa", p="aaaaaaaaaaaaa")
assert [0] == solution.findAnagrams(s="aaaaaaaaaa", p="aaaaaaaaaa")
assert [0, 6] == solution.findAnagrams(s="cbaebabacd", p="abc")
assert [0, 1, 2] == solution.findAnagrams(s="abab", p="ab")
