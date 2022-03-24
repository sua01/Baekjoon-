# 모각코 11일차
# 트리

class Node():
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def get_tree():
  root = Node(7)
  node_2 = Node(3)
  node_3 = Node(10)
  root.left = node_2
  root.right = node_3

  node_4 = Node(1)
  node_5 = Node(5)
  node_2.left = node_4
  node_2.right = node_5

  node_6 = Node(8)
  node_3.left = node_6

  node_7 = Node(4)
  node_5.left = node_7

  node_8 = Node(12)
  node_7.left = node_8

  return root

# 트리 높이 구하기
def get_height(node):
    height = 0
    if(node!=None):
      height = 1 + max(get_height(node.left), get_height(node.right))
    
    return height

# 전위 순회
def pre_order(node):
  if node == None:
      return

  print(f"{node.data}  ", end="")
  pre_order(node.left)
  pre_order(node.right)

root = get_tree()
pre_order(root)
print('트리의 높이는',get_height(root))