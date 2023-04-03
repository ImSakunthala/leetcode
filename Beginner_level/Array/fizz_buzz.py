"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:

1 <= n <= 104
"""


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        int_list = list(range(1, n+1))
        number_list = []

        for number in int_list:

            if number % 3 == 0 and number % 5 == 0:
                number = 'FizzBuzz'
            elif number % 3 == 0:
                number = 'Fizz'
            elif number % 5 == 0:
                number = 'Buzz'
            else:
                number = str(number)

            number_list.append(number)

        return number_list


solution = Solution()
print(solution.fizzBuzz(15))
print(solution.fizzBuzz(3))
print(solution.fizzBuzz(5))
print(solution.fizzBuzz(18))

