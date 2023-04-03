"""You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats
where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time,
provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)


Constraints:
1 <= people.length <= 5 * 104
1 <= people[i] <= limit <= 3 * 104
"""
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # boats -> to keep count of boats with max_capacity
        boats = 0

        # To sort -> to know given maximum weight is less or greater than limit
        people.sort()

        # Using binary search -> we are keeping track of weight of people and limit of boat
        left, right = 0, len(people) - 1

        # loop until we reach the same index
        while left <= right:

            # move left index ->if sum of weight of people in left index and right index is less than or equal to limit
            if people[left] + people[right] <= limit:
                left += 1

            # increase the count of boat and decrease index of right at any cost
            boats += 1
            right -= 1

        return boats


solution = Solution()
assert 5 == solution.numRescueBoats(people=[6, 3, 5, 6, 2, 3], limit=6)
assert 3 == solution.numRescueBoats(people=[3, 2, 3, 2, 2], limit=6)
assert 1 == solution.numRescueBoats(people=[2, 2], limit=6)
assert 4 == solution.numRescueBoats(people=[3, 5, 3, 4], limit=5)
assert 3 == solution.numRescueBoats(people=[3, 2, 2, 1], limit=3)
assert 1 == solution.numRescueBoats(people=[1, 2], limit=3)
