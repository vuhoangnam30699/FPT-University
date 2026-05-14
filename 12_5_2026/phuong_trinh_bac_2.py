# Ví dụ PT bậc 2

a = float(input('A = '))
b = float(input('B = '))
c = float(input('C = '))


delta = b*b-4*a*c

if delta == 0:
    x = -b/(2*a)
    print('Nghiệm kép: X = ', x)
    
elif delta < 0:
    print('Vô nghiệm')
    
else:
    x1 = (-b+delta**0.5)/(2*a)
    x2 = (-b-delta**0.5)/(2*a)
    print('X1 = ', x1)
    print('X2 = ', x2)