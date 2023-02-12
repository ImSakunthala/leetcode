"""
Write a program that takes two numbers as input from the user and divides the first number by the second.
Handle the ZeroDivisionError exception to handle the case where the second number is 0.
"""


class Solution:
    def zero_division(self, numerator: int, denominator: int) -> int or str:
        # try -> block of code in Python that is used to enclose the code that might raise an exception.
        # The purpose of try block is to catch exceptions that are raised in the code,
        # so that they can be handled in a more controlled way, rather than causing the program to crash.
        try:
            result = numerator // denominator

        # except if the denominator is zero we can except zero division error.
        except ZeroDivisionError:
            return 'Value of denominator is Zero'

        # This is final block that executed, if given denominator input is not zero
        return result


solution = Solution()
assert 'Value of denominator is Zero' == solution.zero_division(numerator=5, denominator=0)
assert 2 == solution.zero_division(numerator=4, denominator=2)
