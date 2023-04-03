"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters,
it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        import re

        alphanumeric = re.sub('[^a-zA-Z0-9]', '', s)
        converting_to_lowercase = alphanumeric.lower()
        new_input = converting_to_lowercase[::-1]
        if converting_to_lowercase == new_input:
            return True
        else:
            return False


solution = Solution()
assert True == solution.isPalindrome('ab_a')
assert True == solution.isPalindrome('A man, a plan, a canal: Panama')
assert False == solution.isPalindrome('race a car')
assert True == solution.isPalindrome('')
