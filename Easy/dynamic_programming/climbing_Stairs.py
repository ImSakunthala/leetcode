"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45"""


def climbstairs(n):
    import math

    if 0 < n <= 2:
        return n
    elif 3 <= n <= 45:
        check = n // 2
        result = 1
        for poss in range(1, check + 1):
            result += math.comb(n - poss, poss)
        return result
    else:
        print('Its more than 45 steps!, so given number of steps is exceeds limit')

    return


print(climbstairs(5))
