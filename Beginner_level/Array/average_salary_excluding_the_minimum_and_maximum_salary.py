"""
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual
answer will be accepted.

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000


Constraints:

3 <= salary.length <= 100
1000 <= salary[i] <= 106
All the integers of salary are unique.
"""
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        # Total_sum -> sum of the given salary excluding minimum and maximum salary of the list.
        total_sum = 0
        # minimum salary and maximum salary -> 1000 <= salary[i] <= 106
        min_salary = 1000000
        max_salary = 0

        # iterate through the array and add them to total sum
        for i in salary:
            min_salary = min(min_salary, i)
            max_salary = max(max_salary, i)

            total_sum += i

        # Return 0 -> if given array is empty else return average
        return 0 if len(salary) == 0 else (total_sum - min_salary - max_salary) / (len(salary) - 2)

    def average_1(self, salary: List[int]) -> float:
        # Separate variable for max and min salary and then find sum and total emp000000000loyees
        max_salary = max(salary) if len(salary) > 2 else 0
        min_salary = min(salary) if len(salary) > 2 else 0
        sum_salary = sum(salary) - max_salary - min_salary
        total_employees = len(salary) - 2 if len(salary) > 2 else 1

        return sum_salary / total_employees

    def average_2(self, salary: List[int]) -> float:
        # remove max and min salary from given array and return average
        salary.remove(max(salary))
        salary.remove(min(salary))

        return sum(salary) / len(salary)


solution = Solution()
assert 0 == solution.average(salary=[])
assert 3000.0 == solution.average(salary=[4000, 4000, 3000, 1000, 2000])
assert 2750.0 == solution.average(salary=[4000, 4000, 3000, 1000, 2000, 2000])
assert 2000.0 == solution.average(salary=[1000, 2000, 3000])
assert 4000.0 == solution.average(salary=[4000])
assert 2000.0 == solution.average(salary=[1000, 2000, 3000])