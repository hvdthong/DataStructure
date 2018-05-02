class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


def printList(node):
    while node:
        print node,
        node = node.next
    print


def printBackward(node):
    if node is None:
        return
    else:
        head = node
        tail = node.next
        printBackward(tail)
        print head,


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.next = node2
    node2.next = node3

    printList(node1)
    printBackward(node1)
