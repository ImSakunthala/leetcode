"""Given two integer arrays pushed and popped each with distinct values, return true if this could have been the
result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.


Constraints:

1 <= pushed.length <= 1000
0 <= pushed[i] <= 1000
All the elements of pushed are unique.
popped.length == pushed.length
popped is a permutation of pushed.
"""
from typing import List


class Solution:
    def validateStackSequences1(self, pushed: List[int], popped: List[int]) -> bool:
        # Using two pointers, i -> represent elements in push, j -> represent elements in popped
        i, j = 0, 0

        # iterate through the push element
        for element in pushed:
            # assign element to pushed i pointer
            pushed[i] = element

            # check whether push element and popped element is same and check whether push element and pop element
            # are same, if so, True -> decrease the push pointer by 1 and increase the pop pointer by 1
            while i >= 0 and pushed[i] == popped[j]:
                i = i - 1
                j = j + 1
            # increment the push pointer by one to check next element in pop
            i += 1

        # return if push pointer is zero if so then stack is empty and specified push and pop sequence is correct
        return i == 0

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # Method 2: Using stack
        # create an empty stack
        stack = []

        # j pointer -> represent indices of popped array
        j = 0

        # iterate through the push array and append element to stack
        for element in pushed:
            stack.append(element)

            # if last element of stack is same as pop element then increase the pop pointer by 1 and remove from stack
            while stack and stack[-1] == popped[j]:
                j += 1
                stack.pop()

        # return if stack is empty
        return len(stack) == 0


solution = Solution()
assert False == solution.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2])
assert True == solution.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1])
