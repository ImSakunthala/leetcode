class Solution:
    def input_number_to_list(self, num: int) -> list:
        result = list()
        place_value = 1
        while num > 0:
            unit_digit = num % 10
            result.insert(0, unit_digit * place_value)

            num = num // 10
            place_value *= 10

        return result



    def intToRoman(self, num: int) -> str:
        value_map = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
                     4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM',
                     2: 'II', 3: 'III', 6: 'VI', 7: 'VII', 8: 'VIII'}
        list_of_digits = self.input_number_to_list(num)
        result = ''
        for digit in list_of_digits:
            result += value_map[digit]
        return result



solution = Solution()
print(solution.intToRoman(45))