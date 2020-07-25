class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        # Returns the node's data
        return self.value

    def get_next(self):
        # Returns the next node
        return self.next

    def set_next(self, new_next):
        # Sets the node's next node
        self.next = new_next


class LinkedList:
    def __init__(self):
        # The first node
        self.head = None
        # The last node
        self.tail = None

    def add_to_tail(self, value):
        # Adds data to the end of LinkedList
        new_node = Node(value)
        # Handle empty list
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # Non-empty list
        else:
            # Set the next node on the new node
            self.tail.set_next(new_node)
            # Set the tail to the new node
            self.tail = new_node

    def remove_head(self):
        # Removes the head node and returns the data
        # Save the head node data
        if self.head is None:
            return None
        value = self.head.get_value()
        # Handle the single node
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            # Set the head to the next node
            self.head = self.head.get_next()

        return value

    def contains(self, value):
        if self.head is None:
            return False

        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True

            current_node = current_node.next
        return False

    def get_max(self):
        if self.head is None:
            return None

        current_node = self.head
        max = 0
        while current_node is not None:
            if current_node.value > max:
                max = current_node.value
            current_node = current_node.next
        return max
