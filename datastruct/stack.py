class StackInterface:
    def __init__(self):
        pass

    def push(self, item):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass

    def __str__(self):
        pass

class Stack(StackInterface):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def __str__(self):
        string = ""
        for i, item in enumerate(self.items):
            string += str(item)
            string += "\n"
        
        return string