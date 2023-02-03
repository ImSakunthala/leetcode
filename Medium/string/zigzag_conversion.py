"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to
display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000

"""


class Solution:
    @staticmethod
    def convert(s: str, numRows: int) -> str:
        # If number of rows is greater than or equal to length of string then output will be given input string
        # Create an empty array with given number of rows
        converted_string = [''] * numRows

        # index -> index of the converted string & it should always lie between given number of rows - 1
        # move -> movement of character in zigzag direction
        index, move = 0, 1

        # Using for loop separating each and every character in string
        for char in s:

            # when index and move is positive then it is in forward direction
            # if index reach zero there should be forward movement
            if index == 0:
                move = 1

            # if index exceed given number of rows - 1 then it should move backwards.
            # so reset move to -1
            elif index > numRows - 1:
                move = -1
                index = (index - 1) + move

            # add character to the empty converted string array
            converted_string[index] += char
            # to avoid negative indexing we use absolute
            index = abs(index + move)

        return ''.join(converted_string)


solution = Solution()
assert 'ACEBDF' == solution.convert(s='ABCDEF', numRows=2)
assert 'A' == solution.convert(s='A', numRows=1)
assert 'PAYPALISHIRING' == solution.convert(s='PAYPALISHIRING', numRows=14)
assert 'PINALSIGYAHRPI' == solution.convert(s='PAYPALISHIRING', numRows=4)
assert 'PAHNAPLSIIGYIR' == solution.convert(s='PAYPALISHIRING', numRows=3)
