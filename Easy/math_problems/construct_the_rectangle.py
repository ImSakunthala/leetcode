"""A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area,
your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

The area of the rectangular web page you designed must equal to the given target area.
The width W should not be larger than the length L, which means L >= W.
The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.



Example 1:

Input: area = 4 Output: [2,2] Explanation: The target area is 4, and all the possible ways to construct it are [1,4],
[2,2], [4,1]. But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal
compared to [2,2]. So the length L is 2, and the width W is 2. Example 2:

Input: area = 37
Output: [37,1]
Example 3:

Input: area = 122122
Output: [427,286]


Constraints:

1 <= area <= 107
"""
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # The smallest width is always less than or equal to the square root of the area. For example, if area = 28,
        # then Possible rectangle -> [1,28], [2,14], [4, 7], [7,4] [14,2], [28,1]. condition 1 -> The width W should
        # not be larger than the length L, which means L >= W. so we eliminate -> [7,4], [14,2], [28,1] check the
        # eliminated possible values. [28, 1] , [2, 14], [4,7] -> all the width values are more than sqrt(28),
        # so we delete to get optimal solution sqrt will also easier for us to get The difference between length L
        # and width W should be as small as possible.
        smallest_width = area ** 0.5

        for width in range(int(smallest_width), 0, -1):
            if area % width == 0:
                return [area // width, width]


solution = Solution()
print(solution.constructRectangle(area=122122))
print(solution.constructRectangle(area=4))
print(solution.constructRectangle(area=37))
