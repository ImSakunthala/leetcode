"""
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.


Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters and stars *.
The operation above can be performed on s.
"""


class Solution:
    def removeStars(self, s: str) -> str:
        # create an empty stack to add characters
        result = []

        # Separate index and character using enumerate ->To enumerate object yields pairs containing a count
        # (from start, which defaults to zero) and a value yielded by the iterable argument.
        for index, char in enumerate(s):
            # if character is "*", then remove the last index using pop -> Remove and return item at index (default
            # last), else if index is out of range then raise index Error
            if char == '*':
                result.pop(-1)
            else:
                # Append char to result stack
                result.append(char)

        # return stack as a string using join method
        return ''.join(result)


solution = Solution()
assert '' == solution.removeStars(s="erase*****")
assert 'lecoe' == solution.removeStars(s="leet**cod*e")
assert 'rbio' == solution.removeStars(s="xa**j*z*e*a*q*ry*bioj*mzd**k**g*")