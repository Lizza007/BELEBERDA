s = open('24 (3).txt').readline()
c = 0
m = ''
cnt = 0
a = 0
for i in range (len(s)-1, -1, -1):
    cnt += 1
    if s[i]=='A':
        m +=1
        if m>=c:
            c = m 
            a = cnt
    else: m =0
print(len(s)-a+1)

