class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k # queue에 들어가는 최대 length
        self.q1 = 0 # front 값
        self.q2 = 0 # rear 값

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.q[self.q2] = value
            self.q2 = (self.q2 + 1) % self.maxlen
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.q[self.q1] = None
            self.q1 = (self.q1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.q1] is None else self.q[self.q1]

    def Rear(self) -> int:
        print(self.q2-1)
        print(self.q[self.q2-1])
        return -1 if self.q[self.q2 - 1] is None else self.q[self.q2 - 1]

    def isEmpty(self) -> bool:
        return self.q1 == self.q2

    def isFull(self) -> bool:
        return self.q1 == self.q2 and self.q[self.q1] is not None


class MyCircularQueueBook:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    # enQueue(): 리어 포인터 이동
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    # deQueue(): 프론트 포인터 이동
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()



if __name__ == "__main__":

    myCircularQueue =  MyCircularQueue(3)

    print(myCircularQueue.isFull())
    myCircularQueue.enQueue(10)
    myCircularQueue.enQueue(20)
    print(myCircularQueue.q1)
    print(myCircularQueue.q2)
    myCircularQueue.enQueue(30)

    print(myCircularQueue.q1)
    print(myCircularQueue.q2)
    print(myCircularQueue.Rear())
    print(myCircularQueue.deQueue())
    myCircularQueue.enQueue(40)
    print(myCircularQueue.Rear())
    print(myCircularQueue.deQueue())
    myCircularQueue.enQueue(10)
    print(myCircularQueue.q)
    print(myCircularQueue.q1)
    print(myCircularQueue.q2)
    print(myCircularQueue.isFull())


    print("--------------------------------------")

    myCircularQueueBook = MyCircularQueueBook(3)
    print(myCircularQueueBook.Rear())
    myCircularQueueBook.enQueue(10)
    myCircularQueueBook.enQueue(20)
    print(myCircularQueueBook.p1)
    print(myCircularQueueBook.p2)
    myCircularQueueBook.enQueue(30)
    print(myCircularQueueBook.p1)
    print(myCircularQueueBook.p2)
    print(myCircularQueueBook.Rear())
    print(myCircularQueueBook.deQueue())
    myCircularQueueBook.enQueue(40)
    print(myCircularQueueBook.Rear())
    print(myCircularQueueBook.deQueue())
    myCircularQueueBook.enQueue(10)
    print(myCircularQueueBook.q)
    print(myCircularQueueBook.p1)
    print(myCircularQueueBook.p2)