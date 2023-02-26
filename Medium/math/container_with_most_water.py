"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store. Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        heights = []
        max_area = max(height)

        for num in height:
            if num != max_area:
                heights.append(num)
        max_area1 = max(heights) if len(heights) != 0 else 0

        return max_area**2 if len(heights) == 0 else max_area1**2


solution = Solution()
print('49 ->', solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
print('1 ->', solution.maxArea(height=[1, 1]))
