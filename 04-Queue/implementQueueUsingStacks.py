# python의 list자료구조를 통해 LIFO로 동작하는 Stack구현
class StackADT:
    # empty stack생성.
    def __init__(self):
        self.data = []

    # stack의 top부분에 원소e를 삽입.
    def push(self, e):
        self.data.append(e)

    # stack의 top부분에 있는 원소를 삭제(or 제거) 후, 해당 원소를 return
    # 만약 stack이 empty라면 에러를 return
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self.data.pop()

    # stack의 top부분에 있는 원소를 return
    # 만약 stack이 empty라면 None return
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.data[-1]

    # 만약 stack이 empty라면 True를 return
    def is_empty(self):
        return len(self.data) == 0

    # stack의 size를 return
    def size(self):
        return len(self.data)


class MyQueue:

    def __init__(self):
        self.data = StackADT()

    def push(self, x: int) -> None:
        self.data.push(x)

    def pop(self) -> int:
        return self.data.data.pop(0)

    def peek(self) -> int:
        if len(self.data.data) == 0:
            return None
        else:
            return self.data.data[0]

    def empty(self) -> bool:
        return len(self.data.data) == 0

class MyQueueBook:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# stack으로 queue 구현
if __name__ == "__main__":

    MyQueue = MyQueue()

    MyQueue.push(1) # [1]
    MyQueue.push(2) # [1, 2]
    print(MyQueue.data.data) # [1, 2]
    print(MyQueue.peek())   # 1
    print(MyQueue.pop())    # 1
    print(MyQueue.empty())  # False
    print(MyQueue.pop())  # 2
    print(MyQueue.empty())  # True
