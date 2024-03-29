import random
class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


class Queue:

    def __init__(self):
        self.stack_enqueue = Stack()
        self.stack_dequeue = Stack()

    def is_empty(self):
        return self.stack_enqueue.is_empty() and self.stack_dequeue.is_empty()

    def enqueue(self, item):
        self.stack_enqueue.push(item)

    def dequeue(self):
        if self.stack_enqueue:
            if self.stack_dequeue.is_empty():
                while not self.stack_enqueue.is_empty():
                    self.stack_dequeue.push(self.stack_enqueue.pop())
        return self.stack_dequeue.pop()

    def peek(self):
        if self.stack_dequeue.is_empty():
            while not self.stack_enqueue.is_empty():
                self.stack_dequeue.push(self.stack_enqueue.pop())
        return self.stack_dequeue.peek()


    def size(self):
        return self.stack_enqueue.size()


my_queue = Queue()
for _ in range(10):
    n = random.randint(1, 1000)
    my_queue.enqueue(n)

print('Queue:', my_queue, '\n', [my_queue.dequeue() for i in range(my_queue.size()-1)])


my_stack = Stack()
for _ in range(10):
    n = random.randint(1, 2000)
    my_stack.push(n)

print('\nStack:\n', my_stack, '\n', [my_stack.pop() for i in range(my_stack.size()-1)])



__________________________________________________________________
# Queue: <__main__.Queue object at 0x00000208DC9313A0> 
#  [756, 308, 220, 41, 446, 283, 302, 231, 650]

# Stack:
#  <__main__.Stack object at 0x00000208DC820850> 
#  [170, 258, 1175, 322, 1019, 1289, 271, 948, 130]
