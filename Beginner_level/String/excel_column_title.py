"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

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
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"


Constraints:

1 <= columnNumber <= 231 - 1
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title_map = {i: chr(65 + i) for i in range(26)}
        print(title_map)
        n = columnNumber
        # Create an empty string for storing the characters.
        result = ''

        # Run a loop while n is positive.
        while n > 0:
            # Subtract 1 from n to handle when module of 26 becomes 0 and here mapping of string starts from zero
            n = n - 1
            # Get current character by doing modulo of  n by 26.
            result += title_map[n % 26]
            # Divide n by 26.
            n = n // 26

        # Now reverse the result string because we have found characters from right to left.
        return result[::-1]


solution = Solution()
print('ZY ->', solution.convertToTitle(columnNumber=701))
print('Az ->', solution.convertToTitle(columnNumber=52))
