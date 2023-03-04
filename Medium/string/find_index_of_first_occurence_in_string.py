"""Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""


class Solution:
    def seprate_str(self, haystack: str, needle: str) -> list:
        pairs = []
        for i in range(len(haystack) - len(needle) + 1):
            pairs.append(haystack[i:i + len(needle)])
        return pairs

    def strStr(self, haystack: str, needle: str) -> int:
        needle_in_haystack = self.seprate_str(haystack, needle)
        if needle not in needle_in_haystack:
            return -1
        else:
            for index, needles in enumerate(needle_in_haystack):
                if needles == needle:
                    return index


solution = Solution()
print(solution.strStr(haystack = "sadbutsad", needle = "sad"))
print(solution.strStr(haystack = "leetcode", needle = "leeto"))
