#백준 1157 : 단어 공부

word = input()
alph = [-1 for i in range(26)]

if len(word)>1000000:
    print("문자길이를 초과했습니다.")
    exit()

word = word.lower()
for i in range(len(word)):
    for j in range(len(alph)):
        if ord(word[i])-97==j and alph[j]==-1: #아스키코드 이용해서 구분, 중복된 문자는 첫 숫서로
            alph[j] = i

