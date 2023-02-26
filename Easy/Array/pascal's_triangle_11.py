"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


Constraints:

0 <= rowIndex <= 33
"""
import python_coding.leetcode.pascal_triangle as pascal


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        rows = pascal.Solution().generate(rowIndex)
        print(rows)

        return rows[-1]


solution = Solution()
print(solution.getRow(3))
print(solution.getRow(0))
print(solution.getRow(1))
print(solution.getRow(5))
