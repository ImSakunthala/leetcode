"""
You're given strings jewels representing the types of stones that are jewels, and stones representing
the stones you have. Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.

Letters are case-sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
"""


class Solution:

    def num_of_jewels_in_stones(self, jewels: str, stones: str) -> int:

        total_num_of_jewel_in_stone = 0

        for stone in stones:
            if stone in jewels:
                total_num_of_jewel_in_stone += 1

        return total_num_of_jewel_in_stone


if __name__ == '__main__':
    solution = Solution()
    assert solution.num_of_jewels_in_stones(jewels='aA', stones='aAAbbbb') == 3
    assert solution.num_of_jewels_in_stones(jewels='z', stones='ZZ') == 0
    assert solution.num_of_jewels_in_stones(jewels='Big', stones='Smith') == 1
    assert solution.num_of_jewels_in_stones(jewels='Sakunthala', stones='Ramachandran') == 7
    assert solution.num_of_jewels_in_stones(jewels='Sakunthala', stones='Ilan') == 3
    assert solution.num_of_jewels_in_stones(jewels='Jewel', stones='Stone') == 1
    assert solution.num_of_jewels_in_stones(jewels='', stones='') == 0
    assert solution.num_of_jewels_in_stones(jewels='jewels', stones='') == 0
    assert solution.num_of_jewels_in_stones(jewels='', stones='stones') == 0
    assert solution.num_of_jewels_in_stones(jewels='zzzz', stones='zzZZAA') == 2
    assert solution.num_of_jewels_in_stones(jewels='abcdefgh', stones='AbCdEfGh') == 4
    assert solution.num_of_jewels_in_stones(jewels='zyxw', stones='ZyxW') == 2
    assert solution.num_of_jewels_in_stones(jewels='Ramachandran', stones='Sakunthala') == 5
    assert solution.num_of_jewels_in_stones(jewels='valuable', stones='notes') == 1
    assert solution.num_of_jewels_in_stones(jewels='!@#$%^', stones='!@#$%^') == 6
    assert solution.num_of_jewels_in_stones(jewels='Sa@22', stones='Ram@25') == 3
