"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
import gc


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value)

        # Set new node next to old head and prev to None
        new_node.next = self.head
        new_node.prev = None

        # Handle empty DLL
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return

        # Change old head prev to new node
        if self.head is not None:
            self.head.prev = new_node

        # Set head to new node
        self.head = new_node
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if self.length == 1:
            value = self.head.value
            self.tail = None
            self.head = None
            self.length = 0
        if self.head is not None:
            value = self.head.value
            self.head = self.head.next
            self.prev = None
            self.length -= 1
        return value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value)

        # The new tail next is None
        new_node.next = None

        # Handle empty DLL
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return

        # Reset the old tail and set the new tail
        last = self.tail
        last.next = new_node
        new_node.prev = last
        self.tail = new_node
        self.length += 1

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if self.length == 1:
            value = self.tail.value
            self.tail = None
            self.head = None
            self.length = 0
        if self.tail is not None:
            value = self.tail.value
            self.tail = self.tail.prev
            self.next = None
            self.length -= 1
        return value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # Node is already head node
        if node.prev is None:
            return
        # Node is tail node
        if node.next is None:
            self.add_to_head(node.value)
            self.remove_from_tail()
        # Node is in the middle
        else:
            self.add_to_head(node.value)
            self.delete(node)

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # Node is already tail node
        if node.next is None:
            return
        # Node is head node
        if node.prev is None:
            self.add_to_tail(node.value)
            self.remove_from_head()
        # Node is in the middle
        else:
            self.add_to_tail(node.value)
            self.delete(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # Handle empty dll
        if self.length <= 1:
            self.tail = None
            self.head = None
            self.length = 0
            return
        # Node to delete is head node
        if self.head == node:
            self.head = node.next
        # Change next if node to be deleted is not the tail
        if node.next is not None:
            node.next.prev = node.prev
        # Change prev if node to be deleted in not the head
        if node.prev is not None:
            node.prev.next = node.next
        self.length -= 1
        gc.collect()

    """Returns the highest value currently in the list"""

    def get_max(self):
        max = 0
        node = self.head
        while node is not None:
            if node.value > max:
                max = node.value
            node = node.next
        return max
