# Doubly Linked List 이중 연결 리스트

class Node:
  def init(self, data, Llink=None, Rlink=None):
    self.data = data
    self.Llink = Llink
    self.Rlink = Rlink

class DoublyLinkedList(object):
  def init(self):
    self.head = Node(None)
    self.tail = self.head
    self.size=0

  def listSize(self):
    return self.size

 # idx 위치의 노드 값 가져오기
  def get(self, idx):
    if idx >= self.size:
      print("Index Error")
      return None
    
    if idx == self.size:
      return self.tail
    if idx==0:
      return self.head
    else:
      node = self.head
      for _ in range(idx):
        node = node.Rlink
      return node

  # 리스트 맨 앞에 추가
  def appendLeft(self, data):
    if self.size==0:
      self.head = Node(data)
      self.tail = self.head
    else:
      node = self.head
      new_node = Node(data, Rlink=node)
      node.Llink = new_node
      self.head = new_node

    self.size+=1

  # 리스트 맨 뒤에 추가
  def appendRight(self, data):
    if self.size==0:
      self.head = Node(data)
      self.tail = self.head
    else:
      node = self.tail
      new_node = Node(data, Llink=node)
      node.Rlink = new_node
      self.tail = new_node

    self.size+=1

  # 데이터를 원하는 위치에 추가
  def insert(self, data, idx):
    if self.size==0:
      self.head = Node(data)
      self.tail = self.head

    else:
      node = self.get(idx)
      if node==None:
        return
      if node == self.head:
        self.appendLeft(data)
      elif node == self.tail:
        self.appendRight(data)
      else:
        node_Llink = node.Llink
        new_node = Node(data, node_Llink, node)
        node_Llink.Rlink = new_node
        node.Llink = new_node
    
    self.size += 1

  # idx 위치의 노드 삭제
  def delete(self, idx):
    if self.size == 0:
      print("Empty Linked List")
      return
    else:
      node = self.get(idx)
      if node==None:
        return
      elif node == self.head:
        node = self.head
        self.head = self.head.Rlink
      elif node == self.tail:
        node = self.tail
        self.tail = self.tail.Llink
      else:
        node.Llink.Rlink = node.Rlink
        node.Rlink.Llink = node.Llink
      del(node)
      self.size-=1


  # 연결 리스트 출력
  def print_linked_list(self):
    node = self.head
    while node != self.tail:
      print(node.data,'<->', dne='')
      node = node.Rlink
    print(node.data)