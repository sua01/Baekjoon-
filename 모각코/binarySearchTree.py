# 이진 탐색 트리

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def set_root(self, data):
    self.root = Node(data)

  def find(self, data):
    if self.find_node_by_data(self.root, data) == False:
        return False
    else:
        return True

  def find_node_by_data(self, current_node, data):
    if current_node == None:
        return False
    print(current_node.data)
    if data == current_node.data:
        return current_node

    if data < current_node.data:
        return self.find_node_by_data(current_node.left, data)
    if data > current_node.data:
        return self.find_node_by_data(current_node.right, data)


BST = BinarySearchTree()
BST.set_root(1)

print(BST.root.data)