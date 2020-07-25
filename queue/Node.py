class Node:
    """
    Data: value and next node
    Methods: 
        1. get value
        2. set value
        3. get next
        4. set next
    """

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    """
    Data:
        1. ref to head Node
        2. ref to tail Node

    Behavior/Methods:
        1. Append ( Add a new node to the Node ref'd by the tail)
        2. Prepend ( Add a new node and poiny yjay Node's next_node at the old Head; update Head pointer)
        3. Remove Head
        4. Remove Tail
        5. Contains?
        6. Get Maximum?
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = None
        else:
            head = self.head
            self.head = new_node
            self.head.set_next(head)

    def remove_head(self):
        if self.head is None:
            return None
        elif self.head.get_next() is None:
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        else:
            head = self.head
            self.head = self.head.next_node
            return head.get_value()

    def remove_tail(self):
        if not self.head:
            return None
        elif self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
        value = self.tail.get_value()
        self.tail = current
        self.tail.set_next(None)
        return value

    def contains(self, value):
        if not self.head:
            return False
        # Recursive solution
        # def search(node):
        #   if node.get_value() == value:
        #     return True
        #   if not node.get_next():
        #     return False
        #   return search(node.get_next())
        # return search(self.head)
        # get a reference to the node we're currently at; update this as we traverse the list

        current = self.head

        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):
        if not self.head:
            return None

        # reference to the largest value we've seen so far
        max_value = self.head.get_value()

        # reference to our current node as we traverse the list
        current = self.head.get_next()

        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()

        return max_value
