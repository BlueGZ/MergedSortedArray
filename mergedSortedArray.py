a1 = [1, 2, 3, 6, 9, 7]
b1 = [2, 5, 6, 0]
a = len(a1)
b = len(b1)
c1 = [0 for i in range(a + b)]
for i in range(a):
    c1[i] = a1[i]
for i in range(b):
    c1[i + a] = b1[i]
print(c1)
f = 0
for i in range(a+b):
    if c1[i] == 0:
        f = f + 1
for i in range(f):
    c1.remove(0)
e = len(c1)
for i in range(e):
    for j in range(e):
        if c1[i] < c1[j]:
            d = c1[i]
            c1[i] = c1[j]
            c1[j] = d
print(c1)
