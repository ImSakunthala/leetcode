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
        result = 0

        if len(words) == 1:
            return 1

        else:

            morse_code_words_list = []
            for word in words:
                morse_word = ''
                for character in word:
                    morse_word += morse_code_dict[character]
                morse_code_words_list.append(morse_word)
            print(morse_code_words_list)

            for index, morse_code_word in enumerate(morse_code_words_list):
                if (index + 1) < len(words):
                    a = morse_code_words_list[index]
                    b = morse_code_words_list[index + 1]
                    if a == b:
                        result += 1

        return result


solution = Solution()
# print('2 ->', solution.uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"]))
# print('1 ->', solution.uniqueMorseRepresentations(words=["a"]))
print('1 ->', solution.uniqueMorseRepresentations(words=["noilq", "kzlq", "ydreq", "ybxk", "kzlq"]))
