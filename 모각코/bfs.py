# BFS 탐색

MAX_QUEUE_SIZE = 10

class Queue:
  def __init__(self):
    self.arr = [-1] * MAX_QUEUE_SIZE
    # head : 가장 오래된 데이터의 위치
    # tail : 가장 최근 추가된 데이터의 위치
    self.head = 0
    self.tail = 0

  def is_empty(self):
    if self.head == self.tail:
        return True
    return False

  def is_full(self):
    if (self.tail + 1) % MAX_QUEUE_SIZE == self.head:
        return True
    return False

  def enqueue(self, item):
    if self.is_full():
        print("큐에 더이상 데이터를 넣을 수 없습니다.")
        return -1

    self.tail = (self.tail + 1) % MAX_QUEUE_SIZE
    self.arr[self.tail] = item

  def dequeue(self):
    if self.is_empty():
        print("큐가 비어있습니다.")
        return -1

    self.head = (self.head + 1) % MAX_QUEUE_SIZE
    return self.arr[self.head]

class Graph:
  def __init__(self):
      self.node_count = 7
      self.graph = [
          [0, 1, 0, 1, 0, 0, 0],
          [1, 0, 1, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 1, 0, 1],
          [0, 0, 0, 1, 0, 1, 0],
          [0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
      ]
      self.visited = [0] * self.node_count

def BFS(graph, node):
  queue = Queue()
  graph.visited[node] = 1
  print(node, end=" ")

  queue.enqueue(node)
  while not queue.is_empty():
      v = queue.dequeue()
      for w in range(graph.node_count):
          if graph.graph[v][w] == 1 and graph.visited[w] == 0:
              graph.visited[w] = True
              print(w, end=" ")
              queue.enqueue(w)

graph = Graph()
BFS(graph, 0)