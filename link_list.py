class Node:
    """linked list node"""

    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def add(self, val):
        curr = self
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(val)


class LinkedList:
    """linked list head pointer"""

    def __init__(self, val) -> None:
        self.head = Node(val)

    def pretty_print(self):
        curr = self.head
        while curr is not None:
            print(curr.val)
            curr = curr.next
        print("---")

    def push(self, val):
        if self.head is not None:
            self.head.add(val)

    def remove_head(self):
        if self.head is not None:
            new_head = self.head.next
            self.head.next = None
            self.head = new_head

    def remove_at(self, pos):
        if self.head is not None:
            count = 1
            if pos == 0:
                self.remove_head()
                return
            curr = self.head
            while count < pos and curr.next is not None:
                curr = curr.next
                count += 1
            if curr.next is not None:
                curr.next = curr.next.next

    def remove_by_val(self, val):
        if self.head is not None:
            if self.head.val is val:
                self.remove_head()
                return
            curr = self.head
            while curr.next is not None and curr.next.val is not val:
                curr = curr.next
            if curr.next is not None:
                curr.next = curr.next.next

    def insert_at(self, val, pos):
        count = 0
        curr = self.head
        if curr is not None:
            while count < pos and curr.next is not None:
                curr = curr.next
            to_add = Node(val)
            to_add.next = curr.next
            curr.next = to_add


ll = LinkedList("A")
ll.push("B")
ll.push("C")
ll.pretty_print()
ll.remove_at(1)
ll.pretty_print()
ll.remove_by_val("A")
ll.pretty_print()
