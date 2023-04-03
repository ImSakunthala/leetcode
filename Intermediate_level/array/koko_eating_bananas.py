"""Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone
and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k
bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more
bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23


Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""
from typing import List


class Solution:
    def eating_speed(self, speed: int, piles: list, h: int) -> bool:
        # initialise time to zero
        time = 0
        # calculate time to eat each pile
        for pile in piles:
            time += (pile + speed - 1) // speed
        # return True -> within calculated speed koko can eat pile and move right by middle value
        # False -> calculated speed of koko is less to eat whole pile so move left pointer to middle value
        return time <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # left and right decides -> initialise the middle value (speed of eating) for koko eat bananas.
        left, right = 1, max(piles)

        # while loop -> to do the binary search until speed of eating bananas becomes equal.
        while left < right:
            # fixing speed -> by middle values
            mid = (left + right) // 2
            # to  check whether koko can eat bananas, within the specified time.
            # True -> move right pointer to middle value
            if self.eating_speed(mid, piles, h):
                right = mid
            # False -> move left pointer by one
            else:
                left = mid + 1
        # when both left and right becomes equal return either left or right
        return left


solution = Solution()
assert solution.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5) == 30
assert solution.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6) == 23
assert solution.minEatingSpeed(piles=[3, 6, 7, 11], h=8) == 4

