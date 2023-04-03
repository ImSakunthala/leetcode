"""
A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied
by its satisfaction level i.e. time[i] * satisfaction[i].

Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.



Example 1:

Input: satisfaction = [-1,-8,0,5,-9] Output: 14 Explanation: After Removing the second and last dish, the maximum
total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14). Each dish is prepared in one unit of time.
Example 2:

Input: satisfaction = [4,3,2]
Output: 20
Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
Example 3:

Input: satisfaction = [-1,-4,-5]
Output: 0
Explanation: People do not like the dishes. No dish is prepared.


Constraints:

n == satisfaction.length
1 <= n <= 500
-1000 <= satisfaction[i] <= 1000
"""
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes
        # multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

        max_satisfaction = sorted(satisfaction, reverse=True)

        # result -> sum of time to cook the positive reviewed dish [Note: +ve -> positive like time to cook same dish
        # considering previous time to cook the previous dish]
        # like time -> it is like time coefficient of the dish prepared by chef in a day[given satisfaction array]
        result, like_time = 0, 0

        # loop throughout dish time in list.
        for dish_time in max_satisfaction:

            # like time -> if positive, add time to like time coefficient to given dish time
            like_time += dish_time

            # like time -> if negative, then there is no need of consideration
            if like_time < 0:
                break

            # result -> add result to like time coefficient
            result += like_time

        return result


solution = Solution()
assert 14 == solution.maxSatisfaction(satisfaction=[-1, -8, 0, 5, -9])
assert 20 == solution.maxSatisfaction(satisfaction=[4, 3, 2])
assert 0 == solution.maxSatisfaction(satisfaction=[-1, -4, -5])
