"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ''
        prefix = ''
        common_min_length = len(min(strs, key=len))
        for i in range(common_min_length):
            for idx, element in enumerate(strs):
                if idx == 0:
                    prefix = element[i]
                if prefix == element[i]:
                    continue
                else:
                    break
            else:
                result += prefix
        return result


solution = Solution()
# print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
print(solution.longestCommonPrefix(['cir', 'car']))
