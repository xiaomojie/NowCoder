class Queue:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, node):
        if (not self.queue1 and not self.queue2) or self.queue1:
            self.queue1.append(node)
        else:
            self.queue2.append(node)

    def pop(self):
        if self.queue1:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop(0)
        elif self.queue2:
            while len(self.queue2) >1:
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop(0)
        else:
            return None

queue = Queue()
queue.push('a')
queue.push('b')
queue.push('c')
print(queue.pop())
queue.push('d')
print(queue.pop())
print(queue.pop())
queue.push('e')
print(queue.pop())
print(queue.pop())
