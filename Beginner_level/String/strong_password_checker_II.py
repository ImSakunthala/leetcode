"""
A password is said to be strong if it satisfies all the following criteria:

It has at least 8 characters. It contains at least one lowercase letter. It contains at least one uppercase letter.
It contains at least one digit. It contains at least one special character. The special characters are the characters
in the following string: "!@#$%^&*()-+". It does not contain 2 of the same character in adjacent positions (i.e.,
"aab" violates this condition, but "aba" does not). Given a string password, return true if it is a strong password.
Otherwise, return false.

Example 1:

Input: password = "IloveLe3tcode!"
Output: true
Explanation: The password meets all the requirements. Therefore, we return true.

Example 2:

Input: password = "Me+You--IsMyDream" Output: false Explanation: The password does not contain a digit and also
contains 2 of the same character in adjacent positions. Therefore, we return false.

Example 3:

Input: password = "1aB!"
Output: false
Explanation: The password does not meet the length requirement. Therefore, we return false.


Constraints:

1 <= password.length <= 100
password consists of letters, digits, and special characters: "!@#$%^&*()-+".
"""


class Solution:
    def check_length(self, password: str) -> bool:
        return False if len(password) < 8 else True

    def check_uppercase(self, password: str) -> bool:
        return True if any(character.isupper() for character in password) else False

    def check_lowercase(self, password: str) -> bool:
        return True if any(character.islower() for character in password) else False

    def check_digit(self, password: str) -> bool:
        return True if any(character.isdigit() for character in password) else False

    def special_character(self, password: str) -> bool:
        special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
        for character in password:
            if character in special_characters:
                return True
        else:
            return False

    def check_character_repetition(self, password: str, max_occurrence=2) -> bool:
        prev_character = ''
        current_occurrence = 0

        for char in password:
            if char == prev_character:
                current_occurrence += 1
            else:
                prev_character = char
                current_occurrence = 1

            if current_occurrence != max_occurrence:
                continue
            else:
                return False
        return True

    def strongPasswordCheckerII(self, password: str) -> bool:
        rule_list = [self.check_length(password), self.check_uppercase(password), self.check_lowercase(password),
                     self.check_digit(password), self.special_character(password),
                     self.check_character_repetition(password)]

        for check in rule_list:
            if check == False:
                return False
        return True


solution = Solution()
assert solution.strongPasswordCheckerII(password="11A!A!Aa") == False
assert solution.strongPasswordCheckerII(password = "IloveLe3tcode!") == True
assert solution.strongPasswordCheckerII(password = "Me+You--IsMyDream") == False
assert solution.strongPasswordCheckerII(password = "1aB!") == False