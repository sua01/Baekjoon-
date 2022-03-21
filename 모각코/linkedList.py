# Linked List 연결 리스트

class Node:
  def init(self, data, pointer=None):
    self.data = data
    self.pointer = pointer

class LinkedList(object):
  def init(self):
    self.head = Node(None)
    self.size=0

  def get(self, idx):
    if idx >= self.size:
      print("Index Error")
      return None
    
    if idx==0:
      return self.head
    else:
      node = self.head
      for _ in range(idx):
        node = node.pointer
      return node

  # 데이터를 리스트 마지막에 추가
  def append(self, data):
    if self.size==0:
      self.head = Node(data)
      self.size+=1
    else:
      node = self.head
      while node.pointer!=None:
        node=node.pointer

      new_node = Node(data)
      node.pointer = new_node
      self.size+=1

  # 데이터를 원하는 위치에 추가
  def insert(self, val, idx):
    if self.size==0:
      self.head = Node(val)
      self.size+=1
    elif idx ==0:
      self.head = Node(val, self.head)
      self.size+=1
    else:
      node = self.get(idx-1)
      if node==None:
        return

      new_node = Node(val)
      next_node=node.pointer
      node.pointer = new_node
      new_node.pointer = next_node
      self.size += 1

  # idx 위치의 노드 삭제
  def delete(self, idx):
    if self.size == 0:
      print("Empty Linked List")
      return
    elif idx >= self.size:
      print("Index Error")
      return
    elif idx == 0:
      self.head = self.head.pointer
      self.size -= 1
    else:
      node = self.get(idx - 1)
      node.pointer = node.pointer.pointer
      self.size -= 1

  # 연결 리스트 출력
  def print_linked_list(self):
    node = self.head
    while node:
      if node.pointer != None:
          print(node.data, "-> ", end="")
          node = node.pointer
      else:
          print(node.data)
          node = node.pointer