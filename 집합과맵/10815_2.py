# 백준 집합과 맵 : 10815번 - 숫자 카드

# 반복을 이용한 이진 탐색 이용
def search_binary(list, key, low, high):
  while low <= high:
    mid = (low + high) // 2
    if key == list[mid]:
      return mid
    elif key < list[mid]:
      high = mid - 1
    else:
      low = mid + 1

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