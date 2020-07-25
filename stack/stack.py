"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# set it up with an array for storage

# add and remove from the same side
# pancakes
# plates

from singly_linked_list import LinkedList  # linkedList

# LinkedList implementation


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        if self.size is None:
            return self.size == None
        else:
            return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if len(self) > 0:
            # There are elements in the LinkedList. pop the last one.
            removed_tail = self.storage.remove_tail()
            self.size -= 1
            return removed_tail
        else:
            return None


# # array implementation
# class Stack:
#     def __init__(self):
#         self.size = 0
#         # self.storage = ?
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value) ##0(1)

#     def pop(self):
#         if len(self) > 0:
#             # There are elements in the array. pop the last one.
#             removed = self.storage.pop() ##0(1)
#             return removed
#         else:
#             return None
