"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        string_map = {')': '(', '}': '{', ']': '['}
        stack_data = []
        for ch in s:
            if string_map.keys().__contains__(ch):
                previous_ch = stack_data.pop() if len(stack_data) > 0 else None
                if previous_ch != string_map.get(ch):
                    return False
            else:
                stack_data.append(ch)
        return len(stack_data) == 0


solution = Solution()
print(solution.isValid("([{}])"))
print(solution.isValid("()[]{}"))
print(solution.isValid("([({}[]()){}])"))
print(solution.isValid("([{([({}[]()){}])}]"))
print(solution.isValid(")"))
