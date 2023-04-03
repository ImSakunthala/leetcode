"""
You are given the strings key and message, which represent a cipher key and a secret message, respectively.
The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet),
we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message.

Example 1:
Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Output: "this is a secret"
Explanation: The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog".

Example 2:

Input: key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
Output: "the five boxing wizards jump quickly"
Explanation: The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "eljuxhpwnyrdgtqkviszcfmabo".

Constraints:

26 <= key.length <= 2000
key consists of lowercase English letters and ' '.
key contains every letter in the English alphabet ('a' to 'z') at least once.
1 <= message.length <= 2000
message consists of lowercase English letters and ' '.
"""


class Solution:
    def get_mapping_for_key(self, given_key: str) -> dict:
        import string

        # ascii_lowercase -- a string containing all ASCII lowercase letters
        list_of_alphabets = [alphabet for alphabet in string.ascii_lowercase]

        # to remove space in given_key
        given_key = given_key.replace(' ', '')
        distinct_keys = [key for pos, key in enumerate(given_key) if key not in given_key[:pos]]

        return dict(zip(distinct_keys, list_of_alphabets))


    def decodeMessage(self, key: str, message: str) -> str:
        key_map = self.get_mapping_for_key(key)

        decoded_message = ''
        for character in message:
            decoded_message += key_map[character] if character in key_map.keys() else character

        return decoded_message


solution = Solution()
assert 'this is a secret' == solution.decodeMessage(
    key="the quick brown fox jumps over the lazy dog", message="vkbs bs t suepuv")

assert "the five boxing wizards jump quickly" == solution.decodeMessage(
    key="eljuxhpwnyrdgtqkviszcfmabo", message="zwx hnfx lqantp mnoeius ycgk vcnjrdb")
