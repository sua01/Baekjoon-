# 백준 집합과 맵 : 10815번 - 숫자 카드

# 이진 탐색 이용
def search_binary(list, key, low, high):
  if low <= high:
    mid = (low + high) // 2
    if key == list[mid]:
      return mid
    elif key < list[mid]:
      return search_binary(list, key, low, mid - 1)
    else:
      return search_binary(list, key, mid + 1, high)

  return -1

n = int(input())  # 가지고 있는 숫자 카드 개수
num = list(map(int, input().split())) # 숫자 카드에 적혀있는 정수
m = int(input())# 구별할 숫자 카드 개수
guess_num = list(map(int, input().split()))  # 구별할 숫자 카드에 적혀있는 정수

# 리스트 정렬하기
num.sort()

for i in guess_num:
  if search_binary(num, i, 0, n - 1) == -1: # 포함되지 않은 경우
    print(0, end=' ')
  else: # 포함된 경우
    print(1, end=' ')