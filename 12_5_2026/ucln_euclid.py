# Tính UCLN (thuật toán euclid)

a = int(input('A = '))
b = int(input('B = '))

while (b > 0):
    if (a > b):
        a, b = b, a % b
    else:
        a, b = a, b % a
        
print('Ước số chung lớn nhất là:', a)