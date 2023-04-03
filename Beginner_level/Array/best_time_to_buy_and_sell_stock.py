"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for index, buying_price in enumerate(prices):
            selling_prices = prices[index + 1:]

            selling_price = max(selling_prices) if len(selling_prices) > 0 else 0
            profit = selling_price - buying_price
            max_profit = profit if profit > max_profit else max_profit

        return max_profit


solution = Solution()
print(solution.maxProfit([2, 4, 1]))
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([7, 6, 4, 3, 1]))
print(solution.maxProfit([1]))
print(solution.maxProfit([3, 2, 6, 5, 0, 3]))
