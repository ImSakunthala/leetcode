"""
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:

Input: word = "USA"
Output: true

Example 2:

Input: word = "FlaG"
Output: false

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.capitalize():
            print(word.capitalize())
            return True
        elif word == word.casefold():
            print(word.casefold())
            return True
        elif word == word.upper():
            print(word.upper())
            return True
        else:
            return False




solution = Solution()
print('True ->', solution.detectCapitalUse('USA'))
print('True ->', solution.detectCapitalUse('leetcode'))
print('True ->', solution.detectCapitalUse('Google'))
print('False ->', solution.detectCapitalUse('FlaG'))
