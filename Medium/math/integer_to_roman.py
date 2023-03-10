"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII,
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        # other than given basic roman numeral, roman numeral change its numeral when they reach given below condition.
        # I can be placed before V (5) and X (10) to make 4 and 9.
        # X can be placed before L (50) and C (100) to make 40 and 90.
        # C can be placed before D (500) and M (1000) to make 400 and 900.
        basic_roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
                       10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        # create an empty string.
        result = ''

        # iterate through dictionary, to find the largest Roman numeral that is less than or equal to the number
        for value, numeral in basic_roman.items():
            while num >= value:
                # Add that Roman numeral to the result string and subtract value from current number.
                result += numeral
                num -= value

        return result


solution = Solution()
assert 'III' == solution.intToRoman(num=3)
assert 'XLIV' == solution.intToRoman(num=44)
assert 'MCMXCV' == solution.intToRoman(num=1995)
=======
class Solution:
    def input_number_to_list(self, num: int) -> list:
        result = list()
        place_value = 1
        while num > 0:
            unit_digit = num % 10
            result.insert(0, unit_digit * place_value)

            num = num // 10
            place_value *= 10

        return result



    def intToRoman(self, num: int) -> str:
        value_map = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
                     4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM',
                     2: 'II', 3: 'III', 6: 'VI', 7: 'VII', 8: 'VIII'}
        list_of_digits = self.input_number_to_list(num)
        result = ''
        for digit in list_of_digits:
            result += value_map[digit]
        return result



solution = Solution()
print(solution.intToRoman(45))
