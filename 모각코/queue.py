# 선형 큐
MAX_SIZE = 10

class Queue:
  # 큐 초기화
  def _init(self):
    self.arr = [None]*MAX_SIZE
    self.head = -1
    self.tail = -1

  # 큐 꽉 찼는지 확인
  def is_full(self):
    if self.head >= MAX_SIZE-1:
      return True
    return False
  
  # 큐 비었는지 확인
  def is_empty(self):
    if self.head==self.tail:
      return True
    return False

  def enqueue(self, val):
    if self.is_full():
      print("Queue is full")
      return
    else:
      self.tail+=1
      self.arr[self.tail] = val

  def dequeue(self):
    if self.is_empty():
      print("Queue is empty")
      return
    else:
      self.head+=1
      return self.arr[self.head]
