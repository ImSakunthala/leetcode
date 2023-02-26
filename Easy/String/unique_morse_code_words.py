"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:

[a =".-"],[b ="-..."],[c ="-.-."],[d ="-.."],[e ="."],[f ="..-."],[g ="--."],
[h ="...."],[i =".."],[j =".---"],[k ="-.-"],[l =".-.."],[m ="--"],[n ="-."],
[o ="---"],[p =".--."],[q ="--.-"],[r =".-."],[s ="..."],[t ="-"],[u ="..-"],
[v ="...-"],[w =".--"],[x ="-..-"],[y ="-.--"],[z ="--.."]
Given an array of strings words where each word can be written as a
concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...".
We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.

Example 1:

Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".
Example 2:

Input: words = ["a"]
Output: 1

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 12
words[i] consists of lowercase English letters.
"""


class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_code_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
                           'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-',
                           'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-',
                           'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--',
                           'x': '-..-', 'y': '-.--', 'z': '--..'}

        morse_code_words_list = []
        for word in words:
            morse_word = ''
            for character in word:
                morse_word += morse_code_dict[character]
            if morse_word not in morse_code_words_list:
                morse_code_words_list.append(morse_word)

        return len(morse_code_words_list)


solution = Solution()
assert 2 == solution.uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"])
assert 1 == solution.uniqueMorseRepresentations(words=["a"])
assert 1 == solution.uniqueMorseRepresentations(words=["noilq", "kzlq", "ydreq", "ybxk", "kzlq"])
