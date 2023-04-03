"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.



Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
"""
from typing import List
from itertools import groupby


class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []

        # TIL: groupby tool from itertools This method calculates the keys for each element present in iterable. It
        # returns key and iterable of grouped items. returns -> It returns consecutive keys and groups from the
        # iterable. If the key function is not specified or is None, key defaults to an identity function and returns
        # the element unchanged.

        for char, group in groupby(chars):
            count = len(list(group))
            result.append(char)
            if count > 1:
                result.extend(list(str(count)))
        chars[:] = result

        return len(result)


solution = Solution()
assert solution.compress(chars=["a", "a", "a", "b", "b", "a", "a"]) == 6
assert solution.compress(chars=["a", "a", "b", "b", "c", "c", "c"]) == 6
assert solution.compress(chars=["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) == 4
assert solution.compress(chars=["a"]) == 1
