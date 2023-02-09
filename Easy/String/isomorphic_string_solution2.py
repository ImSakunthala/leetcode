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
    def string_map(self, string: str) -> str:

        string_map = {}
        key_count = 1

        for character in string:
            if character not in string_map:
                string_map[character] = key_count
                key_count += 1

        transformed_string = '-'.join(str(string_map[ch]) for ch in string)

        print(f'input:{string} output:{transformed_string}')

        return transformed_string

    def isIsomorphic(self, s: str, t: str) -> bool:

        string_1 = self.string_map(s)
        string_2 = self.string_map(t)

        if string_1 == string_2:
            return True
        else:
            return False


solution = Solution()
print(solution.isIsomorphic('egg', 'add'))
print(solution.isIsomorphic('aaabbbba', 'bbbaaaba'))
print(solution.isIsomorphic('paper', 'title'))
print(solution.isIsomorphic('foo', 'bar'))
