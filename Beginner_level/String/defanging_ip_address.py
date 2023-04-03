"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".



Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"


Constraints:

The given address is a valid IPv4 address.
"""


class Solution:
    def defangIPaddr1(self, address: str) -> str:
        result = address.replace('.', '[.]')
        return result

    def defangIPaddr2(self, address: str) -> str:
        new_address = ''

        split_address = address.split('.')

        separator = '[.]'

        new_address = separator.join(split_address)

        return new_address


solution = Solution()
print('1[.]1[.]1[.]1 -> ', solution.defangIPaddr1('1.1.1.1'))

print('1[.]1[.]1[.]1', solution.defangIPaddr1('1.1.1.1'))
print(solution.defangIPaddr1('255.100.50.0'))
print(solution.defangIPaddr2('128.000.000.1'))
print(solution.defangIPaddr2('192.000.000.1'))
print(solution.defangIPaddr2('100.0.0.1'))
