class Tree:

    class Node:

        def __init__(self, data):
            self._data = data
            self._children = []

        def __str__(self):
            return str(self.data)

        def get_data(self):
            return self._data

        def set_data(self, data):
            self._data = data

        def get_children(self):
            return self._children

        def add_child(self, child):
            self._children.append(child)

        def remove_child(self, child):
            self._children.remove(child)

        def is_leaf(self):
            return self._children == []

        def __eq__(self, other):
            return self._data == other.get_data()

        def __str__(self):
            return str(self._data)

    
    def __init__(self):
        self._root = None

    def set_root(self, root):
        self._root = root

    def get_root(self):
        return self._root

    def _str_node(self, node, level:int=0):
        string = "  " * level + str(node) + "\n"
        for child in node.get_children():
            string += self._str_node(child, level + 1)

        return string

    def find(self, data):
        return self._find(self._root, data)

    def _find(self, node, data):
        if node == data:
            return node

        for child in node.get_children():
            found = self._find(child, data)
            if found:
                return found

        return None

    def __str__(self):
        return self._str_node(self._root)

class BinaryTree(Tree):

    class BinaryNode:
            
        def __init__(self, data):
            self._data = data
            self._left = None
            self._right = None

        def __str__(self):
            return str(self.data)

        def get_data(self):
            return self._data

        def set_data(self, data):
            self._data = data

        def get_left(self):
            return self._left

        def set_left(self, left):
            self._left = left

        def get_right(self):
            return self._right

        def set_right(self, right):
            self._right = right

        def is_leaf(self):
            return self._left == None and self._right == None

        def __eq__(self, other):
            return self._data == other.get_data()

        def __str__(self):
            return str(self._data)



        
