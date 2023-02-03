"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters,
return true if sentence is a pangram, or false otherwise.

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:

Input: sentence = "leetcode"
Output: false


Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""
import string


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        list_of_characters = [character for character in string.ascii_lowercase]
        sentence_characters = set(character for character in sentence)

        if len(list_of_characters) == len(sentence_characters):
            return True
        else:
            return False

    def check_if_panagram(self, sentence: str) -> bool:

        counter = [0] * 26

        for char in sentence:
            counter[ord(char) - 97] += 1
        print(counter)

        for num in counter:
            if num == 0:
                return False
        else:
            return True


solution = Solution()
print('True ->', solution.check_if_panagram(sentence = "thequickbrownfoxjumpsoverthelazydog"))
print('False ->', solution.check_if_panagram(sentence= "leetcode"))
print('False ->',  solution.check_if_panagram(sentence= 'anmt'))