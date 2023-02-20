"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_count = Counter(s)

        for index, char in enumerate(s):
            if s_count[char] == 1:
                return index
        else:
            return -1


solution = Solution()
assert 0 == solution.firstUniqChar(s="leetcode")
assert 2 == solution.firstUniqChar(s='loveleetcode')
assert -1 == solution.firstUniqChar(s='aabb')
