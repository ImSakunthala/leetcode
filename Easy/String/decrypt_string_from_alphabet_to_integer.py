"""
You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.



Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"


Constraints:

1 <= s.length <= 1000
s consists of digits and the '#' letter.
s will be a valid string such that mapping is always possible.
"""
import string


class Solution:
    def freqAlphabets(self, s: str) -> str:

        s = s.replace('10#', 'j').replace('11#', 'k').replace('12#', 'l').replace('13#', 'm').replace('14#',
                                                                                                      'n').replace(
            '15#', 'o')
        s = s.replace('16#', 'p').replace('17#', 'q').replace('18#', 'r').replace('19#', 's').replace('20#',
                                                                                                      't').replace(
            '21#', 'u')
        s = s.replace('22#', 'v').replace('23#', 'w').replace('24#', 'x').replace('25#', 'y').replace('26#',
                                                                                                      'z')
        s = s.replace('1', 'a').replace('2', 'b').replace('3', 'c').replace('4', 'd').replace('5', 'e').replace(
            '6', 'f').replace('7', 'g')
        s = s.replace('8', 'h').replace('9', 'i')

        return s


solution = Solution()
print(solution.freqAlphabets(s="12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
print(solution.freqAlphabets(s="10#11#12"))
print(solution.freqAlphabets(s = "1326#"))