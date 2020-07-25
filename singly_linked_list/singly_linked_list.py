# print("=============================================\n")
# print("===============CLASS EXAMPLE=================\n")
# # good class
# class Dog:
#     def __init__(self, name, status, cuteness = 0):
#         self.name = name
#         self.status = status
#         self.cuteness = cuteness

#     def __str__(self):
#         return f"Name: {self.name}, Status: {self.status}, Cuteness: {self.cuteness}"

# dogs = {
#     "toby": Dog("toby", "good", 10),
#     "crumbs": Dog("crumbs", "good", 11),
#     "cobo": Dog("cobo", "good", 10)

# }

# print(dogs["crumbs"])


# print("\n\n")
# print("==============================================\n")
# print("============CONSTANT EXAMPLE==================\n")


# # constant rtc
# # doesnt depend on the size of input/elements/list size
# commands = ['n', 's', 'e', 'w']
# print(commands[0])


# print("\n\n")
# print("===============================================\n")
# print("============QUADRATIC EXAMPLE==================\n")


# # quadratic
# # print out every combo of pairs of commands
# for counter, x in enumerate(commands):
#     for y in commands:
#         print(counter, x, y)

# print("\n\n")
# print("===============================================\n")
# print("============ENEUMERATE EXAMPLE==================\n")

# # enumerate

# my_list = ["one", "two", "three", "four", "five", "six"]

# for counter, x in enumerate(my_list):         # also u can use key!
#     print(counter, x)

print("\n\n")
print("===============================================\n")
print("============Linked List EXAMPLE==================\n")


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


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        # if empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head is None and self.tail is None:
            return
        # what if we only have a single elem in the linked list?
        # both head and tail are pointing at the same Node
        if not self.head.get_next():
            value = self.head.get_value()  # study this!!! this is a better way to seek data
            # delete the linked list's head reference
            self.head = None
            # also delete the linked list's tail reference
            self.tail = None
            return value
        val = self.head.get_value()
        # set self.head to the Node after the head
        self.head = self.head.get_next()
        return val

    def contains(self, value):
        if not self.head:
            return False
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
