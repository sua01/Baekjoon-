#백준 1316 : 그룹 단어 체커

num = int(input()) # 단어 개수 입력받기

res = 0
for _ in range(num):
    word = input()
    for i in range(len(word)-1):
        if word[i] != word[i+1]:


print(res)