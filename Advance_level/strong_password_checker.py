"""
A password is considered strong if the below conditions are all met:

It has at least 6 characters and at most 20 characters.
It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
It does not contain three repeating characters in a row (i.e., "Baaabb0" is weak, but "Baaba0" is strong).
Given a string password, return the minimum number of steps required to make password strong.
if password is already strong, return 0.

In one step, you can:

Insert one character to password,
Delete one character from password, or
Replace one character of password with another character.

Example 1:

Input: password = "a"
Output: 5
Example 2:

Input: password = "aA1"
Output: 3
Example 3:

Input: password = "1337C0d3"
Output: 0


Constraints:

1 <= password.length <= 50
password consists of letters, digits, dot '.' or exclamation mark '!'.
"""


class Effort:
    def __init__(self, insertion: int = 0, deletion: int = 0, replacement: int = 0):
        self.insertion = insertion
        self.deletion = deletion
        self.replacement = replacement

    def __str__(self):
        return f'Effort(insertion{self.insertion},deletion={self.deletion},replacement={self.replacement})'


class Solution:
    def apply_length_rule(self, password: str, min_length: int = 6, max_length: int = 20) -> Effort:
        if len(password) < min_length:
            insertion_effort = min_length - len(password)
            return Effort(insertion=insertion_effort)
        if len(password) > max_length:
            deletion_effort = len(password) - max_length
            return Effort(deletion=deletion_effort)
        if min_length <= len(password) <= max_length:
            return Effort()

    def apply_lowercase_character_rule(self, password: str) -> Effort:
        if any(character.islower() for character in password):
            return Effort()
        else:
            return Effort(insertion=1)

    def apply_uppercase_character_rule(self, password: str) -> Effort:
        if any(character.isupper() for character in password):
            return Effort()
        else:
            return Effort(insertion=1)

    def apply_digits_rule(self, password: str) -> Effort:
        if any(character.isdigit() for character in password):
            return Effort()
        else:
            return Effort(insertion=1)

    def apply_character_repetition_rule(self, password: str, max_occurrence: int = 3) -> Effort:
        deletion_effort = 0
        prev_character = ''
        current_occurrence = 0

        for char in password:
            if char == prev_character:
                current_occurrence += 1
            else:
                prev_character = char
                current_occurrence = 1

            if current_occurrence == max_occurrence:
                deletion_effort += 1
                prev_character = ''
                current_occurrence = 0

        return Effort(deletion=deletion_effort)

    def strongPasswordChecker(self, password: str) -> int:

        length_effort = self.apply_length_rule(password)
        lowercase_effort = self.apply_lowercase_character_rule(password)
        uppercase_effort = self.apply_uppercase_character_rule(password)
        digit_effort = self.apply_digits_rule(password)
        repeated_characters_effort = self.apply_character_repetition_rule(password)

        steps = 0

        # get max_insertion
        max_insertion = max(length_effort.insertion,
                            sum([lowercase_effort.insertion, uppercase_effort.insertion, digit_effort.insertion]))
        if max_insertion == 0:
            steps += max(length_effort.deletion, repeated_characters_effort.deletion)
        else:


        if repeated_characters_effort.deletion > length_effort.deletion:
            if max_insertion == 0:
                steps += repeated_characters_effort.deletion
            else:
                steps += max_insertion - repeated_characters_effort.deletion
        else:
            steps += length_effort.deletion



        # get max_deletion
        effort_deletion = repeated_characters_effort.deletion - max_insertion
        max_deletion = length_effort.deletion

        # get effective_replacement
        effective_replacement = min(max_insertion, max_deletion)
        # get effective_insertion
        effective_insertion = max_insertion - effective_replacement
        # get effective_deletion
        effective_deletion = max_deletion - effective_replacement
        # steps = sum of effective
        steps = effective_replacement + effective_deletion + effective_insertion

        if 6 <= len(password) <= 20:
            return steps
        else:
            return max_insertion + max_deletion


solution = Solution()
assert 2 == solution.strongPasswordChecker('Passswordsss')
assert 2 == solution.strongPasswordChecker('aaaAAA')
assert solution.strongPasswordChecker('aaa') == 3
assert 5 == solution.strongPasswordChecker('Sakunthala!Ramachandran22')
assert 2 == solution.strongPasswordChecker('SAKUNTHALA')
assert 0 == solution.strongPasswordChecker('1337C0d3')
assert 1 == solution.strongPasswordChecker('Passwordsss')
assert 1 == solution.strongPasswordChecker('Passssword')
assert 1 == solution.strongPasswordChecker('Passsssword')
assert 2 == solution.strongPasswordChecker('ABABABABABABABABABAB1')


