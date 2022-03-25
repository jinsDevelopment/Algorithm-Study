class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top is None:
            return None

        node = self.top
        self.top = self.top.next

        return node.item

    def is_empty(self):
        return self.top is None


if __name__ == "__main__":
    s = Stack()

    s.push(1)

    print(s.top)
    print(s.pop())
    # intArray = [73,74,75,71,69,72,76,73]

