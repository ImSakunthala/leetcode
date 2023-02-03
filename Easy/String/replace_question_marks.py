"""Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters
into lowercase letters such that the final string does not contain any consecutive repeating characters. You cannot
modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution,
return any of them. It can be shown that an answer is always possible with the given constraints.

Example 1:

Input: s = "?zs" Output: "azs" Explanation: There are 25 solutions for this problem. From "azs" to "yzs",
all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in
"zzs".
Example 2:

Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will
consist of consecutive repeating characters in "ubvvw" and "ubvww".


Constraints:

1 <= s.length <= 100
s consist of lowercase English letters and '?'.
"""
import random
import string


class Solution:
    def modifyString(self, s: str) -> str:

        idx = 0
        while idx < len(s):
            if s[idx] == '?':
                left = s[idx-1] if idx > 0 else ''
                right = s[idx+1] if idx < len(s)-1 else ''
                substitute_ch = self.get_substitute_char(left, right)
                s = s[:idx] + substitute_ch + s[idx+1:]
            idx += 1

        return s

    def get_substitute_char(self, left_ch:str, right_ch:str) -> str:
        possibilities = [ch for ch in string.ascii_lowercase if ch not in (left_ch, right_ch)]

        if left_ch in possibilities:
            possibilities.remove(left_ch)
        if right_ch in possibilities:
            possibilities.remove(right_ch)

        return random.choice(possibilities)


solution = Solution()
print(solution.modifyString("j?qg??b"))