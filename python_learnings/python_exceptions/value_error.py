"""
Write a program that reads a list of integers from the user, and prints the average of the numbers.
Handle the ValueError exception to handle the case where the user enters non-integer values.
"""


class Solution:
    def value_error(self, nums: list):
        # while loop -> repeatedly ask user to enter input

        while True:

            # try block -> to get the multiple input from user.
            try:
                number = int(input('Enter number or double enter to stop:'))
                nums.append(number)

            # value error -> if user given no inputs or other than integers
            # calculate average -> for user inputs
            except ValueError:
                if len(nums) == 0:
                    return 'Entered no numbers or Value Error'
                else:
                    average = sum(nums) / len(nums)
                    return 'The average is', average


solution = Solution()
print(solution.value_error(nums=[]))
