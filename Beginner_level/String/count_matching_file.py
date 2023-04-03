"""
You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color,
and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.

Example 1:

Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],
ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

Example 2:

Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],
ruleKey = "type", ruleValue = "phone"
Output: 2
Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.

Constraints:

1 <= items.length <= 104
1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
ruleKey is equal to either "type", "color", or "name".
All strings consist only of lowercase letters.
"""

from typing import List
from collections import defaultdict


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        item_map = defaultdict(list)

        for item in items:
            item_map['type'].append(item[0])
            item_map['color'].append(item[1])
            item_map['name'].append(item[2])
        if ruleKey == 'type':
            return item_map['type'].count(ruleValue)
        if ruleKey == 'color':
            return item_map['color'].count(ruleValue)
        if ruleKey == 'name':
            return item_map['name'].count(ruleValue)


solution = Solution()
print('2 ->', solution.countMatches(
    items=[["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
    ruleKey="type", ruleValue="phone"))
print('1 ->', solution.countMatches(
    items=[["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone","gold", "iphone"]],
    ruleKey="color", ruleValue="silver"))
