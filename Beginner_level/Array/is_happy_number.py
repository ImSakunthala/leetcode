"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 231 - 1
"""


class Solution:
    @staticmethod
    def split_number(n: int) -> list:
        list_of_digits = []
        while n > 0:
            last_digit = n % 10
            list_of_digits.insert(0, last_digit)
            n = n // 10

        return list_of_digits

    @staticmethod
    def square_list(digits: list) -> list:
        list_of_squares = []
        for digit in digits:
            list_of_squares.append(digit * digit)

        return list_of_squares

    @staticmethod
    def sum_of_numbers(digits: list) -> int:
        sum_of_digits = 0
        for digit in digits:
            sum_of_digits += digit

        return sum_of_digits

    def isHappy(self, n: int) -> bool:
        known_sum = []
        final_sum = n

        while final_sum not in known_sum:
            known_sum.append(final_sum)

            list_of_digits = self.split_number(final_sum)
            list_of_square_digits = self.square_list(list_of_digits)
            final_sum = self.sum_of_numbers(list_of_square_digits)

            if final_sum == 1:
                return True

        return False


solution = Solution()
print(solution.isHappy(12345))
