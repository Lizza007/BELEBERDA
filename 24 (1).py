s = open('24 (1).txt').readline()
d = {x:0 for x in sorted(set(s))}
for i in range(len(s)-2):
    if s[i]=='A' and s[i+2]=='F':
        d[s[i+1]]+=1
cnt = 0
word = ''
for a in d:
    if d[a]>cnt:
        cnt = d[a] 
        word = 'A'+a+'F' 
print(word, cnt)


