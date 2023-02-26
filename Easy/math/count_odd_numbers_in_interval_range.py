"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).



Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].


Constraints:

0 <= low <= high <= 10^9
"""


class Solution:
    def count_Odds(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            if num % 2 != 0:
                count += 1
        return count

    def odds_count(self, low: int, high: int) -> int:
        if low%2 == 0 and high%2 == 0:
            return (high - low)//2
        if low % 2 != 0 or high % 2 != 0:
            return (high - low)//2 + 1

    def countOdds(self, low: int, high: int) -> int:
        return (high+1)//2 - (low//2)


solution = Solution()
assert 86213013 == solution.countOdds(low=798273637, high=970699662)
assert 3 == solution.countOdds(low=3, high=7)
assert 1 == solution.countOdds(low=8, high=9)
