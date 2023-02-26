class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Initialize a dictionary to store the frequency of characters in string s
        s_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        # Iterate through the characters in string t
        for char in t:
            if char not in s_dict or s_dict[char] == 0:
                return char
            else:
                s_dict[char] -= 1
        # If no character is found, return None
        return ''


solution = Solution()
print(solution.findTheDifference(s="abcd", t="abcde"))
print(solution.findTheDifference(s="", t="y"))
print(solution.findTheDifference(s="a", t="aa"))
