def fibo(a) :
    res = [] * (a + 1)
    f0, f1 = 0, 1
    res.append(f0)
    for i in range(2, a + 1):
        f0, f1 = f1, f0 + f1
        res.append(f0)
    return res
n = int(input())
a = fibo(n)
for i in a[:-1]:
    print(i, end=",")
print(a[-1])