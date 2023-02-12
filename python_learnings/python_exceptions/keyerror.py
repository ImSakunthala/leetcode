"""
Write a program that takes names and ages from user as input, and print the age of name given by user.
Handle the KeyError exception to handle the case where a name is not found in the dictionary.
"""


class Solution:
    def key_error(self, name_list: dict):
        print('Data Initialization')

        while True:
            name = input('Enter Name[Hit Enter to complete Database initialisation]:')
            if len(name) != 0:
                age = int(input(f'Enter age of {name}'))
                name_list[name] = age
            else:
                break
        print(f'number of records {len(name_list)}')
        print('Data verification')

        while True:
            name = input('Enter name for verification:')
            try:
                if len(name) == 0:
                    print('Bye!')
                    break
                else:
                    print(f'Record found and Age of {name}:', name_list[name])
            except KeyError:
                print('Record Not found in database')


solution = Solution()
print(solution.key_error(name_list={}))



