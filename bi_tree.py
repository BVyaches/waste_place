class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, self)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, self)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def delete(self, data):
        if data == self.data:
            if self.left is None and self.right is None:
                if self.parent.left and self.parent.left.data == data:
                    self.parent.left = None
                else:
                    self.parent.right = None

            elif self.left is None and self.right:
                if self.parent.left and self.parent.left.data == data:
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right

            elif self.right is None:
                if self.parent.left and self.parent.left.data == data:
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left

            else:
                node = self.left
                while self.parent:
                    node = self.right
                self.data = node.data
                if node.parent.left and node.parent.left.data == data:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left

        elif data > self.data:
            self.right.delete(data)
        else:
            self.left.delete(data)

    def find_max(self):
        if self.right:
            self.right.find_max()
        else:
            return self.data

    def find_min(self):
        if self.left:
            self.left.find_min()
        else:
            return self.data


root = Node(12, None)
root.insert(6)
root.insert(3)
root.insert(14)
root.insert(1)
root.insert(5)
root.insert(2)
root.print_tree()
print(root.find_max())
print(root.find_min())
root.delete(6)
root.print_tree()
