#백준 2941 : 크로아티아 알파벳

text = input()

alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alph:
    text = text.replace(i,"*")
print(len(text))