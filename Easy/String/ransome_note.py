"""Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from
magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazine_ch = Counter(magazine)
        ransomNote_ch = Counter(ransomNote)
        result = ''
        for ch in ransomNote:
            if magazine_ch[ch] >= ransomNote_ch[ch]:
                result += ch
        if result == ransomNote:
            return True
        return False


solution = Solution()
print(solution.canConstruct(ransomNote="fihjjjjei", magazine="hjibagacbhadfaefdjaeaebgi"))
print(solution.canConstruct(ransomNote="aab", magazine="baa"))
print(solution.canConstruct(ransomNote="a", magazine="b"))
print(solution.canConstruct(ransomNote="aa", magazine="ab"))
print(solution.canConstruct(ransomNote="aa", magazine="aab"))
