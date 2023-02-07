"""You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are
represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of
fruit each basket can hold. Starting from any tree of your choice, you must pick exactly one fruit from every tree
(including the start tree) while moving to the right. The picked fruits must fit in one of your baskets. Once you
reach a tree with fruit that cannot fit in your baskets, you must stop. Given the integer array fruits, return the
maximum number of fruits you can pick.

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].


Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length
"""
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Create an empty dictionary to store fruits only in two baskets
        baskets = {}

        # initialize first tree to zero
        position, total_fruits = 0, 0

        for index, tree in enumerate(fruits):

            # get() -> Return the value for key if key is in the dictionary, else default. If default is not given,
            # it defaults to None, so that this method never raises a KeyError. Here default value is Zero.
            baskets[tree] = baskets.get(tree, 0) + 1

            # check if length of baskets dictionary is greater than 2, if not then continue to next tree
            # Otherwise, decrease the value of the first tree by -1 and check if it is zero, if so,
            # delete the first tree[k, v] from the basket and increase the position of the first tree t0 1
            if len(baskets) > 2:
                baskets[fruits[position]] -= 1

                if baskets[fruits[position]] == 0:
                    del baskets[fruits[position]]

                position += 1

            # since index starts with zero
            total_fruits = index - position + 1

        return total_fruits


solution = Solution()
assert 3 == solution.totalFruit(fruits=[1, 2, 1])
assert 3 == solution.totalFruit(fruits=[0, 1, 2, 2])
assert 4 == solution.totalFruit(fruits=[1, 2, 3, 2, 2])
assert 5 == solution.totalFruit(fruits=[3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4])
