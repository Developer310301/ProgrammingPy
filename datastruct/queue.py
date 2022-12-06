class QueueInterface:
    def __init__(self):
        pass

    def enqueue(self, item):
        pass

    def dequeue(self):
        pass

    def is_empty(self):
        pass

    def size(self):
        pass

    def __str__(self):
        pass

class Queue(QueueInterface):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        string = ""
        for i, item in enumerate(self.items):
            string += str(item)
            string += "\n"

        return string
