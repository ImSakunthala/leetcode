"""Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace
and initial word order.
Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:

Input: s = "God Ding"
Output: "doG gniD"


Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        reverse_list = []

        for word in s:
            reverse_list.append(word[::-1])

        return " ".join(reverse_list)


solution = Solution()
assert "s'teL ekat edoCteeL tsetnoc" == solution.reverseWords(s="Let's take LeetCode contest")
assert "doG gniD" == solution.reverseWords(s="God Ding")