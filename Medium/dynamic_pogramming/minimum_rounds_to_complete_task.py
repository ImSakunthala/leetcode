"""
You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task.
In each round, you can complete either 2 or 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks,
or -1 if it is not possible to complete all the tasks.

Example 1:

Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4
Explanation: To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2.
- In the second round, you complete 2 tasks of difficulty level 3.
- In the third round, you complete 3 tasks of difficulty level 4.
- In the fourth round, you complete 2 tasks of difficulty level 4.
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.

Example 2:

Input: tasks = [2,3,3]
Output: -1
Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.

Constraints:

1 <= tasks.length <= 105
1 <= tasks[i] <= 109
"""


class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        from collections import Counter

        minimum_rounds = 0

        task_map = dict(Counter(tasks))
        # Counter: dictionary subclass that gives number of occurrence of key

        for task in task_map:

            if task_map[task] == 1:
                return -1

            elif (task_map[task] % 3) == 0:
                minimum_rounds += task_map[task] // 3

            elif (task_map[task] % 3) != 0:
                minimum_rounds += (task_map[task] // 3) + 1
                # for minimum rounds the occurrence of task, divide the occurrence by 3
                # whatever remainder (may be 1/2/3/4/5...) minimum rounds will always be quotient + 1
                # For example:1) if occurrence is 4 [2+2, so minimum rounds = 2], 4//3 -> q:1, r:1 so minimum rounds q+1
                # Example 3: if occurrence is 5 [2+3, so minimum rounds = 2], 5//3 -> q:1, r:1 so minimum rounds q+1
                # Example 3: if occurrence is 7 [2+2+3, so minimum rounds = 3], 7//3 -> q:2, r:1 so minimum rounds q+1

        return minimum_rounds


solution = Solution()
assert 4 == solution.minimumRounds(tasks=[2, 2, 3, 3, 2, 4, 4, 4, 4, 4])
assert -1 == solution.minimumRounds(tasks=[2, 3, 3])
