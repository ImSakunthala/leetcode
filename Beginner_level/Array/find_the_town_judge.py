"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.


Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
"""

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # since the person in town is always given number of people
        person_trust_someone = [0] * n
        person_trusted_by_another = [0] * n

        for person1, person2 in trust:
            # since the index start from zero
            person1 -= 1
            person2 -= 1

            # to indicate that person is either trusted by someone or by another
            person_trust_someone[person1] += 1
            person_trusted_by_another[person2] += 1

        for person in range(n):
            if person_trust_someone[person] == 0 and person_trusted_by_another[person] == n - 1:
                return person + 1  # range starts from zero
        else:
            return -1


solution = Solution()
print('-1 ->', solution.findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]))
print('2 ->', solution.findJudge(n=2, trust=[[1, 2]]))
print('3->', solution.findJudge(n=3, trust=[[1, 3], [2, 3]]))
print('3 ->', solution.findJudge(n=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))

