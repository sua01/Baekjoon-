# 원형 큐

MAX_SIZE = 10

class Queue:
  # 큐 초기화
  def _init(self):
    self.arr = [None]*MAX_SIZE
    self.front = 0
    self.rear = 0

  # 큐 꽉 찼는지 확인
  def is_full(self):
    if (self.rear+1) % MAX_SIZE == self.front:
      return True
    return False
  
  # 큐 비었는지 확인
  def is_empty(self):
    if self.front==self.rear:
      return True
    return False

  def enqueue(self, val):
    if self.is_full():
      print("Queue is full")
      return
    else:
      self.rear = (self.rear + 1) % MAX_SIZE
      self.arr[self.rear] = val

  def dequeue(self):
    if self.is_empty():
      print("Queue is empty")
      return
    else:
      self.front = (self.front + 1) % MAX_SIZE
      return self.arr[self.front]