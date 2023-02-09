"""You are given a string s of even length. Split this string into two halves of equal lengths,
and let a be the first half and b be the second half.
Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
Notice that s contains uppercase and lowercase letters.
Return true if a and b are alike. Otherwise, return false.

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.


Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters."""


def get_vowels(data: str) -> list:
    vowels = ('A', 'E', 'I', 'O', 'U')
    result = []
    for letter in data.upper():
        if letter in vowels:
            result.append(letter)
    return result


def halvesAreAlike(s: str) -> bool:
    divided_string = len(s)
    if divided_string % 2 != 0:
        print("Input string doesn't have equal parts")
    else:
        first_half, second_half = slice(0, (divided_string // 2)), slice((divided_string // 2), divided_string)
        a, b = s[first_half], s[second_half]

        vowels_of_prefix = get_vowels(a)
        vowels_of_suffix = get_vowels(b)

        return len(vowels_of_prefix) == len(vowels_of_suffix)


print(halvesAreAlike('book'))
