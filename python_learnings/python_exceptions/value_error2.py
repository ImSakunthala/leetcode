"""
Write a program that takes a list of strings and converts them to integers.
Handle the ValueError exception to handle the case where a string cannot be converted to an integer.
"""


class Solution:
    def string_to_int(self, string_list: list) -> list:
        result = []
        try:
            for num in string_list:
                result.append(int(num))
        except ValueError:
            print('List contains inconvertible types!')

        return result


solution = Solution()
print(solution.string_to_int(string_list=['1', 'a', 'b', '3']))
assert [1, 2, 3, 4] == solution.string_to_int(string_list=['1', '2', '3', '4'])
