from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    # Add element to end of list
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Add element to beginning of list
    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # Add element after element in the list
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    # Delete a node in the list with a given key
    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            curr_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    # Delete a node in the list given a position in the list
    def delete_node_at_position(self, position):
        cur_node = self.head

        if position == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        counter = 1
        while cur_node and counter != position:
            prev = cur_node
            cur_node = cur_node.next
            counter += 1

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    # Computing the length of a given linked list iteratively
    def len_iterative(self):
        counter = 0
        cur_node = self.head

        while cur_node:
            counter += 1
            cur_node = cur_node.next
        return counter

    # Computing the length of a given linked list recursively
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    # Swap nodes
    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        # Obtain the first key and the previos node
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        # Obtain the second key and the previous node
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def print_helper(self, node, name):
        if node is None:
            print(f"{name} : None")
        else:
            print(f"{name} : {node.data}")

    # List reverse iterative
    # A -> B -> C -> D -> 0
    # D -> C -> B -> A -> 0
    # D <- C <- B <- A -< 0
    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            self.print_helper(prev, "PREV")
            self.print_helper(cur, "CUR")
            self.print_helper(nxt, "NXT")
            print("\n")
            prev = cur
            cur = nxt

        self.head = prev

    # List reverse recursive
    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    # Merge two sorted singly linked list
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        new_head = None
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = new_head
        llist.head = None


llist_1 = LinkedList()
llist_2 = LinkedList()

# llist_1.append(1)
# llist_1.append(5)
# llist_1.append(7)
# llist_1.append(9)
# llist_1.append(10)

# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)

llist_1.append(2)
llist_1.append(3)
llist_1.append(4)
llist_1.append(6)
llist_1.append(8)


llist_2.append(1)
llist_2.append(5)
llist_2.append(7)
llist_2.append(9)
llist_2.append(10)


llist_1.merge_sorted(llist_2)
llist_1.print_list()

# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")

# llist.reverse_recursive()
# llist.reverse_iterative()
# llist.swap_nodes("A", "B")
# print(llist.len_recursive(llist.head))
# print(llist.len_iterative())

# llist.insert_after_node(llist.head.next, "E")
# llist.delete_node("B")
# llist.delete_node_at_position(3)
# llist.print_list()
