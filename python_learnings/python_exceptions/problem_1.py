"""
Write a program that takes two numbers as input from the user and divides the first number by the second.
Handle the ZeroDivisionError exception to handle the case where the second number is 0.
"""


class Solution:
    def zero_division(self, numerator: int, denominator: int) -> int or str:
        try:
            result = numerator // denominator

        except ZeroDivisionError:
            return 'Value of denominator is Zero'

        return result


solution = Solution()
assert 'Value of denominator is Zero' == solution.zero_division(numerator=5, denominator=0)
assert 2 == solution.zero_division(numerator=4, denominator=2)
