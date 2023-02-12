"""
Write a program that takes two lists and returns the common elements between the lists.
Handle the IndexError exception to handle the case where one of the lists is shorter than the other.
"""


class Solution:
    def index_error(self, List_1:list, List_2:list) -> list:
        common = []
        if len(List_1) == len(List_2):
            for element in List_2:
                if element in List_1:
                    common.append(element)

        else:
            try:
                raise IndexError
            except IndexError:
                if len(List_1) < len(List_2):
                    print('List_1 is shorter than List_2')
                else:
                    print('List_2 is shorter than List_1')
        return common


solution = Solution()
print(solution.index_error(List_1=[1,2,3], List_2=[2,3,4]))
print(solution.index_error(List_1=[1], List_2=['a','b']))
print(solution.index_error(List_1=[1,2,3,4], List_2=[1,2]))