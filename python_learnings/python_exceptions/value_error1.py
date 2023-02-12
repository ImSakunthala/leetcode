"""
Write a program that takes a list of numbers and prints the largest and smallest numbers in the list.
Handle the ValueError exception to handle the case where the list is empty.
"""


class Solution:
    def value_error(self, nums: list) -> int or str:
        # use max and min get largest and smallest in nums.
        try:
            return 'The largest and smallest in list are', max(nums), min(nums)
        # value error -> if there is no elements in list
        except ValueError:
            if len(nums) == 0:
                return 'There is zero elements in list'


solution = Solution()
assert 'There is zero elements in list' == solution.value_error(nums=[])
assert ('The largest and smallest in list are', 5, 1) == solution.value_error(nums=[1, 2, 3, 4, 5])
assert ('The largest and smallest in list are', 'b', 'a') == solution.value_error(nums=['a', 'b'])
