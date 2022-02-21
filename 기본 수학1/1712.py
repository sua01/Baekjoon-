#백준 1712 : 손익분기점

a, b, c = map(int, input().split())

if b >= c: #손익분기점 존재X
    print(-1)
else:   ##손익분기점 존재
    print(int(a/(c-b) + 1))