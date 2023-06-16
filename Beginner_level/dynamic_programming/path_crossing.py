"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east,
or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously
visited. Return false otherwise.

Example 1:


Input: path = "NES"
Output: false
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:


Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coordinate_x, coordinate_y = 0, 0
        direction = [[0, 0]]

        direction_map = {'N': 1, 'S': -1, 'E': 1, 'W': -1}

        for dir in path:
            if dir == 'N' or dir == 'S':
                coordinate_y += direction_map[dir]
            else:
                coordinate_x += direction_map[dir]

            if [coordinate_x, coordinate_y] in direction:
                return True

            direction.append([coordinate_x, coordinate_y])

        return False


solution = Solution()
print(solution.isPathCrossing(path="NNSWWEWSSESSWENNW"))
print(solution.isPathCrossing(path="NES"))
print(solution.isPathCrossing(path="NESWW"))
