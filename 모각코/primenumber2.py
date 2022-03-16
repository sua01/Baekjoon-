# 모각코 7일차
# 연속된 소수의 합으로 소수 만들 수 있는지?

def prime(n):
  prime_range = n+1
  global prime_list
  prime_list = [True]*prime_range

  sqrt = int(n**0.5) # 제곱근
    
  for i in range(2, sqrt+1):
    if prime_list[i]: # i가 소수인 경우
      # i이후의 i배수들 False로 지우기
      for j in range(2*i, prime_range, i):
        prime_list[j] = False


def answer(n):
  prime(n)
  list = []

  for i in range(2, n+1):
    if prime_list[i]:
      list.append(i)
      if sum(list)==n:
        print("연속된 소수 ", list, "의 합은 ", n, "입니다.")
        break
  else:
    print("연속된 소수의 합으로 ", n,"을 만들 수 없습니다.")

answer(41)
answer(20)