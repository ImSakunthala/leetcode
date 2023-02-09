"""
You own a Goal Parser that can interpret a string command.
The command consists of an alphabet of "G", "()" and/or "(al)" in some order.
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al".
The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"


Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.
"""


class Solution:
    def interpret(self, command: str) -> str:

        result = command.replace('G', 'G')
        result = result.replace('()', 'o')
        result = result.replace('(al)', 'al')

        return result


    def  interpret_using_map(self, command: str) -> str:

        command_map = {'G': 'G', '()': 'o', '(al)': 'al'}

        for key, value in command_map.items():
            command = command.replace(key, value)

        return command





solution = Solution()
print('Gooooal ->', solution.interpret_using_map('G()()()()(al)'))
print('alGalooG ->',solution.interpret_using_map("(al)G(al)()()G"))
print('Goal ->', solution.interpret_using_map("G()(al)"))
