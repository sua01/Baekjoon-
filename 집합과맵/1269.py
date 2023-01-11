# 백준 집합과 맵 : 1269번 - 대칭 차집합

n, m = map(int, input().split())  # 집합 A, B의 원소의 개수 입력받기

a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a-b) + len(b-a))