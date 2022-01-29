#백준 10809 : 알파벳 찾기

alph = [-1 for i in range(26)]
c = input()

for i in range(len(c)):
    for j in range(len(alph)):
        if ord(c[i])-97==j and alph[j]==-1: #아스키코드 이용해서 구분, 중복된 문자는 첫 숫서로
            alph[j] = i

for i in range(len(alph)):
    print(alph[i], end=' ')