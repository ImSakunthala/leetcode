"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701


Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        title_map = {chr(64 + i): i for i in range(1, 27)}
        result = 0

        for index, char in enumerate(columnTitle[::-1]):
            num = title_map[char]
            result += num * (26**index)

        return result


solution = Solution()
print('701 ->', solution.titleToNumber('ZY'))
print('52 ->', solution.titleToNumber('AZ'))
print('28 ->', solution.titleToNumber('AB'))