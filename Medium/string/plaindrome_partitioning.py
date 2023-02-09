"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = [character for character in s]
        result.append(partition)

        for index, character in enumerate(s):
            print(index, character)

        return result


solution = Solution()
print(solution.partition('aab'))