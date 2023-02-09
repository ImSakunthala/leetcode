"""
You are given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position
moves to indices[i] in the shuffled string.

Return the shuffled string.

Example 1:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
Example 2:

Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.


Constraints:

s.length == indices.length == n
1 <= n <= 100
s consists of only lowercase English letters.
0 <= indices[i] < n
All values of indices are unique.
"""


class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:

        string_indices_pairs = []
        for val_ch in zip(indices, s):
            string_indices_pairs.append(val_ch)
        string_indices_pairs.sort()

        transformed_string = ''
        for pair in string_indices_pairs:
            for item in pair:
                if type(item) == str:
                    transformed_string += item

        return transformed_string

    def string_transformation(self, s: str, indices: list[int]) -> str:

        list_of_string = [''] * len(s)
        for index, character in zip(indices, s):
            list_of_string[index] = character

        return ''.join(list_of_string)


solution = Solution()
print('leetcode ->', solution.string_transformation(s='codeleet', indices=[4, 5, 6, 7, 0, 2, 1, 3]))

