"""
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one
row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".



Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]


Constraints:

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase).
"""
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard_1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        keyboard_2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        keyboard_3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        result = []

        for word in words:
            word_1 = set(alpha.lower() for alpha in word)
            if (word_1 & keyboard_1 == word_1) or (word_1 & keyboard_2 == word_1) or (word_1 & keyboard_3 == word_1):
                result.append(word)

        return result


solution = Solution()
assert ['Alaska', 'Dad'] == solution.findWords(words=["Hello", "Alaska", "Dad", "Peace"])

