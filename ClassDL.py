# Markhus Dammar
# 3/3/2020
# This is the class file for Double Linked Lists
# Includes Adding/Removing from Head/End of lists


class ListNode:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

    def __repr__(self):
        return repr(self.data)


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.first = ListNode
        self.last = ListNode

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return str(nodes)

    def push_head(self, new_data):
        new_node = ListNode(data = new_data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.pev = new_node
        self.head = new_node

    def push_end(self, data):
        new_node = ListNode(data = data)
        curr = self.head
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def pop_head(self):
        new_node = self.head
        self.head = new_node.next
        return new_node.data

    def pop_end(self):
        new_node = None
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        curr.prev.next = None
