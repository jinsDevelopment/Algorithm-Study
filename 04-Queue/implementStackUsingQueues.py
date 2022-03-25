import collections

# Python의 list자료구조를 통해 FIFO로 동작하는 Queue구현
class QueueADT:
    # 비어있는 Queue생성
    def __init__(self):
        self.item = []

    # Q에 뒷부분으로 원소x를 삽입(=추가)한다.
    def enqueue(self, x):
        self.item.insert(0, x)

    # Q에 원소를 삭제(=제거)한다.
    # 만약, Q가 비어있다면 에러를 return
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        else:
            return self.item.pop()

    # Q에 첫번째 원소를 return
    # 만약 Q가 비어있다면 None return
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.item[-1]

    # Q가 비어있다면 True를 return
    def is_empty(self):
        return len(self.item) == 0

    # Q의 크기를 return
    def size(self):
        return len(self.item)

class MyStack:

    def __init__(self):
        self.data = QueueADT()

    def push(self, x: int) -> None:
        self.data.enqueue(x)

    def pop(self) -> int:
        return self.data.item.pop(0)

    def top(self) -> int:
        return self.data.item[0]

    def empty(self) -> bool:
        return len(self.data.item) == 0


class MyStackBook:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


if __name__ == "__main__":

    # 후입선출
    MyStack = MyStack()

    MyStack.push(1) # [1]
    MyStack.push(2) # [2, 1]
    print(MyStack.data.item) # [2, 1]
    print(MyStack.top()) # 2
    print(MyStack.pop()) # 2
    print(MyStack.top()) # 1
    print(MyStack.empty()) # False
