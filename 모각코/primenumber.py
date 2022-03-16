# 소수 구하기
# 에라토스테네스의 체

# 소수 개수 구하기
def prime(n):
  prime_range = n+1
  prime_list = [True]*prime_range

  sqrt = int(n**0.5) # 제곱근
    
  for i in range(2, sqrt+1):
    if prime_list[i]: # i가 소수인 경우
      # i이후의 i배수들 False로 지우기
      for j in range(2*i, prime_range, i):
        prime_list[j] = False

  return prime_list.count(True)-2

print("소수 개수는", prime(50000))