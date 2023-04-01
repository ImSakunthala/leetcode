"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)


Constraints:

0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.
"""


class MyHashSet:

    def __init__(self):
        self.data = {}

    def hash_key(self, value: int) -> str:
        return 'mykey_' + str(value)

    def add(self, value: int) -> None:
        if not self.contains(value):
            self.data[self.hash_key(value)] = value

    def remove(self, value: int) -> None:
        if self.contains(value):
            del self.data[self.hash_key(value)]

    def contains(self, key: int) -> bool:
        return self.hash_key(key) in self.data


myHashSet = MyHashSet()

myHashSet.add(1)
assert [1] == list(myHashSet.data.values())

myHashSet.add(2)
assert [1, 2] == list(myHashSet.data.values())

assert myHashSet.contains(1) == True

assert myHashSet.contains(3) == False

myHashSet.add(2)
assert [1,2] == list(myHashSet.data.values())

assert myHashSet.contains(2) == True

myHashSet.remove(2)
assert [1] == list(myHashSet.data.values())

assert myHashSet.contains(2) == False
