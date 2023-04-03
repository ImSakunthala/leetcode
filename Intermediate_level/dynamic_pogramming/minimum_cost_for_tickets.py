"""You have planned some train traveling one year in advance. The days of the year in which you will travel are given
as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.



Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.


Constraints:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
"""
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        # days_array -> to store the total pass rate for maximum of days in the given days array
        # to calculate it for the last day we have added + 1 to it
        days_array = [0] * (max(days) + 1)

        # Precautionary measure: travel days -> to avoid the repetition of given days we are calculating it for set
        # of given days it is totally optional

        # travel_days = set(days)

        # traverse through the days_array to update with the minimum costs
        for i in range(1, len(days_array)):

            # if the day is not the travel day then update it with the previous day value
            if i not in days:

                days_array[i] = days_array[i - 1]

            # if it is a travel day then, calculate the minimum costs for travel day using the costs for single,
            # seven and thirty day pass
            else:

                single_day_pass = days_array[i - 1] + costs[0]
                seven_days_pass = days_array[max(0, i - 7)] + costs[1]
                thirty_day_pass = days_array[max(0, i - 30)] + costs[2]

                # update days array with the minimum costs
                days_array[i] = min(single_day_pass, seven_days_pass, thirty_day_pass)

        # return the last value of the days array -> represents minimum cost for it
        return days_array[-1]


solution = Solution()
assert 11 == solution.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15])
assert 17 == solution.mincostTickets(days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs=[2, 7, 15])
