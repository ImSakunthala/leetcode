"""In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if
the given words are sorted lexicographically in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz" Output: false Explanation: The first three
characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" >
"app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More
info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order_map = {}

        for char, index in enumerate(order, start=1):
            order_map[index] = char

        for word_1, word_2 in zip(words, words[1:]):
            for char_1, char_2 in zip(word_1, word_2):
                if order_map[char_2] < order_map[char_1]:
                    return False
                if order_map[char_2] > order_map[char_1]:
                    return True


solution = Solution()
assert True == solution.isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz")
assert False == solution.isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz")
assert False == solution.isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz")
