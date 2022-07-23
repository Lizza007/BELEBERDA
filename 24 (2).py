m0 = 0
m = 0
l = 10**10 
for s in open('24 (2).txt'):
    s = s.strip()
    for i in range(len(s)):
        if 65 <=ord(s[i]) <=90:
            m0 += 1
    if m <= m0:
        if m == m0:
            l = min(l, len(s)) 
        else:
            l = len(s)
        m = m0 
    m0 = 0
print(l)
            

