"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and
a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split_the_string = s.split()

        pattern_map = {}
        word_map = {}

        if len(pattern) == len(split_the_string):

            for ch_1, ch_2 in zip(pattern, split_the_string):

                if (ch_1 in pattern_map and pattern_map[ch_1] != ch_2) or (ch_2 in word_map and word_map[ch_2] != ch_1):
                    return False

                pattern_map[ch_1] = ch_2
                word_map[ch_2] = ch_1

            return True

        else:
            return False


solution = Solution()
print(solution.wordPattern('abba', 'dog cat cat fish'))
