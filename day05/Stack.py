from day05.Node import Node


class Stack:
    def __init__(self):
        self.root = Node("root")
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def front(self):
        if self.is_empty():
            raise Exception("Empty stack Exception")
        return self.root.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.root.next
        self.root.next = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Empty stack Exception")

        removed_node = self.root.next
        self.root.next = self.root.next.next
        self.size -= 1
        return removed_node.value

    def __str__(self):
        cur = self.root.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]
