class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue:", self.queue)

q = Queue()
q.enqueue(5)
q.enqueue(10)
q.display()
print(q.dequeue())
q.display()