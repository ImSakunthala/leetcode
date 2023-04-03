"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import List


class Solution:
    def addTwoNumbers(self, l1: [List], l2: [List]) -> [List]:
        number_1 = 0
        number_2 = 0

        for index, num in enumerate(l1):
            number_1 += 10 ** index * num
        for index, num in enumerate(l2):
            number_2 += 10 ** index * num

        add_number = number_1 + number_2

        result = []
        while add_number > 0:
            add_number, remainder = divmod(add_number, 10)
            result.insert(0, remainder)
        return [0] if result == [] else result[::-1]


solution = Solution()
assert [7, 0, 8] == solution.addTwoNumbers(l1=[2, 4, 3], l2=[5, 6, 4])
assert [0] == solution.addTwoNumbers(l1=[0], l2=[0])
assert [8, 9, 9, 9, 0, 0, 0, 1] == solution.addTwoNumbers(l1=[9, 9, 9, 9, 9, 9, 9], l2=[9, 9, 9, 9])
