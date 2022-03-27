# 유효한 괄호 쌍 판정하기

# 스택 사용
class Stack:
  def init(self):
    self.arr=[None]*10
    self.top = -1

  def is_empty(self):
    if self.top == -1:
      return True
    else: return False

  def push(self, val):
    self.top+=1
    self.arr[self.top] = val

  def pop(self):
    if self.is_empty():
        return
    else:
      val = self.arr[self.top]
      self.top-=1
      return val

# 괄호 유효한지 판정
def validate_brace_pair(brace):
  stack = Stack()
  stack.init()

  for i in brace:
    stack.push(i)
  
  if stack.pop()=="{":
    print("유효하지 않은 중괄호 쌍입니다.")
  else:
    left = 0
    right = 1

    for _ in range(len(brace)-1):
      if stack.pop()=="}":
        right+=1
      else:
        left+=1
    
    if left==right:
      print("유효한 중괄호 쌍입니다.")
    else:
      print("유효하지 않은 중괄호 쌍입니다.")


validate_brace_pair("{{}}{}")
validate_brace_pair("{{}")
validate_brace_pair("{{{}}}")
validate_brace_pair("}{{{}}}{")