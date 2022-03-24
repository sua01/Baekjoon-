# 우선순위 큐

MAX_HEAP_SIZE = 101

class Heap:
  def __init__(self):
    self.arr = [None] * MAX_HEAP_SIZE
    self.heap_count = 0

  def compare_with_parent(self, index):
    if index <= 1:
        return False
    parent_index = index // 2
    if self.arr[index] < self.arr[parent_index]:
        return True
    else:
        return False

  def insert(self, data):
    self.heap_count += 1
    if self.heap_count == 1:
        self.arr[self.heap_count] = data
        return

    self.arr[self.heap_count] = data
    insert_index = self.heap_count

    while self.compare_with_parent(insert_index):
        parent = insert_index // 2
        self.arr[insert_index], self.arr[parent] = (
            self.arr[parent],
            self.arr[insert_index],
        )

        insert_index = parent
    # print(self.arr[1 : self.heap_count + 1])
    return True

  def compare_with_child(self, index):
    left = 2 * index
    right = 2 * index + 1

    if self.arr[left] == None and self.arr[right] == None:
        return False

    if self.arr[right] == None:
        if self.arr[left] < self.arr[index]:
            return left
        else:
            return False

    if self.arr[left] < self.arr[right]:
        return left
    else:
        return right

  def pop(self):
    index = 1
    root = self.arr[1]

    terminal_data = self.arr[self.heap_count]
    self.arr[self.heap_count] = None
    self.arr[index] = terminal_data
    self.heap_count -= 1

    while True:
        child_index = self.compare_with_child(index)
        if not child_index:
            break

        self.arr[child_index], self.arr[index] = (
            self.arr[index],
            self.arr[child_index],
        )
        index = child_index

    return root

heap = Heap()
work_dict={}

# 우선순위와 작업 입력받기
for _ in range(6):
  priority, work = input("우선순위와 작업 입력>> ").split(' ',1)
  work_dict[int(priority)] = work
  heap.insert(int(priority))

print(work_dict[heap.pop()])
print(work_dict[heap.pop()])
print(work_dict[heap.pop()])