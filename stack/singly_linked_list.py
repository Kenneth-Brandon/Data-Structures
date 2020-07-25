
print("========================NODE==================")

# constructor
# get_value, returns value
# get_next, returns self.next value
# set_next, sets self.next to a new_next


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


# constructor

# add_tail
# remove_head
# contains
# get_max

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_tail(self):
        if not self.head:
            return None

        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        return value

    def remove_head(self):
        if self.head is None and self.tail is None:
            return
        # what if we only have a single elem in the linked list?
        # both head and tail are pointing at the same Node
        if not self.head.get_next():
            head = self.head
            # delete the linked list's head reference
            self.head = None
            # also delete the linked list's tail reference
            self.tail = None
            return head.get_value()
        val = self.head.get_value()
        # set self.head to the Node after the head
        self.head = self.head.get_next()
        return val

    # def contains(self, value):
    #     if not self.head:
    #         return False
    #     # get a reference to the node we're currently at; update this as we traverse the list
    #     current = self.head
    #     # check to see if we're at a valid node
    #     while current:
    #         # return True if the current value we're looking at matches our target value
    #         if current.get_value() == value:
    #             return True
    #         # update our current node to the current node's next node
    #         current = current.get_next()
    #     # if we've gotten here, then the target node isn't in our list
    #     return False

    # def get_max(self):
    #     if not self.head:
    #         return None
    #     # reference to the largest value we've seen so far
    #     max_value = self.head.get_value()
    #     # reference to our current node as we traverse the list
    #     current = self.head.get_next()
    #     # check to see if we're still at a valid list node
    #     while current:
    #         # check to see if the current value is greater than the max_value
    #         if current.get_value() > max_value:
    #             # if so, update our max_value variable
    #             max_value = current.get_value()
    #         # update the current node to the next node in the list
    #         current = current.get_next()
    #     return max_value
