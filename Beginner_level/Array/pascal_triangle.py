"""
Question No: 118
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
"""


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        final_list = [[1]]

        for row in range(numRows - 1):
            last_row = final_list[-1]
            imaginary_row = [0] + last_row + [0]
            new_row = []
            length_of_new_row = len(last_row) + 1

            for position in range(length_of_new_row):
                element = imaginary_row[position] + imaginary_row[position + 1]
                new_row.append(element)

            final_list.append(new_row)

        return final_list

    def print_triangle(self, final_list: list[list[int]]) -> None:
        n = len(final_list)
        no_of_corner_spaces = 2
        no_of_space_bw_elements = n - 1
        max_width = no_of_corner_spaces + n + no_of_space_bw_elements

        for row in final_list:
            elements = ' '.join(str(element) for element in row)
            print(f'{elements:^{max_width}s}')


if __name__ == '__main__':
    solution = Solution()
    result = solution.generate(5)
    solution.print_triangle(result)
