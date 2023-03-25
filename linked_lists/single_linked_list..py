from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size_list = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = node

        self.size_list += 1

    def size(self):
        return self.size_list

    def iter(self):
        current = self.head

        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.head
        previous = self.head

        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    previous.next = current.next
                    self.size_list -= 1
                    return current.data
            previous = current
            current = current.next

    def search(self, data):
        found = False
        for node in self.iter():
            if data == node:
                print(f"Data {data} found!")
                found = True

        if not found:
            print(f"Data {data} not found!")

    def clear(self):
        self.head = None
        self.head = None
        self.size_list = 0

    # Print values in the linked list
    def show(self):
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next

    # Searching a node
    def search_node(self, item):
        probe = self.head
        while probe != None and item != probe.data:
            probe = probe.next

        if probe != None:
            print(f"Target item {item} has been found!")
        else:
            print(f"Target item {item} is not in the linked list!")

    # Replace data in a node with other data
    def replace_node(self, item, new_item):
        probe = self.head

        while probe != None and item != probe.data:
            probe = probe.next

        if probe != None:
            probe.data = new_item
            print(f"{new_item} replaced the old value {item} in the node")
        else:
            print(f"The target item {item} is not in the linked list")

    # Insert node at the beginning of the list
    def insert_node_begin(self, data):
        self.head = Node(data, self.head)

    # Insert new node in the end of the list
    def insert_node_ending(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            probe = self.head
            while probe.next != None:
                probe = probe.next
            probe.next = new_node

    # Delete the node at beginning of the list
    def delete_node_begin(self):
        removed_item = self.head.data
        self.head = self.head.next
        print(f"The node {removed_item} was deleted")

    # Delete the node in the end of the list
    def delete_node_end(self):
        removed_item = self.head.data
        if self.head.next is None:
            self.head = None
        else:
            probe = self.head
            while probe.next.next != None:
                probe = probe.next
            removed_item = probe.next.data
            probe.next = None

        print(f"The node {removed_item} was deleted")

    # Add node in determined position
    def add_node_position(self, item, index):

        if self.head is None or index < 0:
            self.head = Node("Py", self.head)
        else:
            probe = self.head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            probe.next = Node(item, probe.next)

    # Delete node in determined position
    def delete_node_position(self, index):

        if index <= 0 or self.head.next is None:
            removed_item = self.head.data
            self.head = self.head.next
            print(f"The node {removed_item} was deleted")
        else:
            probe = self.head
            while index > 1 and probe.next.next != None:
                probe = probe.next
                index -= 1
            removed_item = probe.next.data
            probe.next = probe.next.next
            print(f"The node {removed_item} was deleted ")

llist = SinglyLinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.show()

# Insert node at the beginning
llist.insert_node_begin("Z")
print("List with new node at the beginning")
llist.show()
# Search a node
llist.search_node("C")
# Replace a node
llist.replace_node("B", "F")

print("New list")
llist.show()

# Insert node in the end
llist.insert_node_ending("H")
print("List with new node in the end")
llist.show()

# Delete the node beginning of the list
llist.delete_node_begin()
print("New list with node deleted at beginnining")
llist.show()

# Delete the node in the end of the list
llist.delete_node_end()
print("New list with node deleted in the end")
llist.show()

# Add node in position 3
llist.add_node_position("P", 3)
print("New list with new node added in position 3")
llist.show()

# Delete the node in position 1
llist.delete_node_position(1)
print("New list without the node in position 1 ")
llist.show()
