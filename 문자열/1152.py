#백준 1152 : 단어의 개수

text = input()

if len(text)>1000000:
    print("잘못 입력했습니다.")
else:
    words = text.split(' ')
    cnt = 0

    for i in words:
        if i.isalpha():
            cnt+=1

print(cnt)