#백준 1157 : 단어 공부

word = input()
alph = [0 for i in range(26)]

if len(word)>1000000:
    print("문자길이를 초과했습니다.")
    exit()

word = word.lower()
for i in range(len(word)):
    for j in range(len(alph)):
        if ord(word[i])-97==j: #아스키코드 이용해서 구분
            alph[j]+=1

most = alph[0]
index = 0
for i in range(len(alph)):
    if most < alph[i]:
        most = alph[i]
        index = i

n=0
for i in range(len(alph)):
    if most == alph[i]:
        n+=1

if(n < 2):
    print(chr(index+65))
else:
     print("?")