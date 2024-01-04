a = open('input.txt', 'r', encoding='utf-8')
j = a.readline().strip()
s = a.readline().strip()

d = 0
for ch in s:
    if ch in j:
        d += 1
b = open('output.txt','w')
b.write(repr(d))
b.close()
"""a = open('input.txt', 'r', encoding='utf-8')
a = open('output.txt','w')
a.write(repr(d))
a.close()"""
