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


#더 좋은 풀이! split()은 공백이 여러개라도 1개로 처리한다.
#word = input()
#print(len(word.split()))