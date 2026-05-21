# In ra các số tự nhiên chia hết cho 7 và nhỏ hơn 1000
n = 0
while n < 1000:
        if (n % 7) == 0:
            print(n)
        n += 1
        
#Tính tổng các số nhỏ hơn 1000 và không chia hết cho 3
t = 0
n = 0
while n < 1000:
    if (n % 3) != 0:
        t = t + n
    n += 1
print(t)