#백준 1157 단어공부 간단하게 풀어보기

word = input().upper()
re = list(set(word)) # 중복된 문자 제거

cnt_list = []
for i in re:
    cnt = word.count(i) # 중복된 문자 개수 몇개인지 계산
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1: # 가장 많이 사용된 문자가 여러 개 존재하는 경우
    print("?")
else:
    print(re[cnt_list.index(max(cnt_list))])