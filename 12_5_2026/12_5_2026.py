# name = input('Tên: ')
# 
# print('Tôi tên là ' + name)
# 
# age = int(input('Tuổi: '))
# 
# print('Tôi %d tuổi' %age)


# if (age >= 18):
#     if (age <= 100):
#         print('Đủ tuổi bầu cử')
#     else:
#         print('Quá tuổi bầu cử')
# else:
#     print('Chưa đủ tuổi')


# Ví dụ PT bậc 2

# a = float(input('A = '))
# b = float(input('B = '))
# c = float(input('C = '))
# 
# 
# delta = b*b-4*a*c
# 
# if delta == 0:
#     x = -b/(2*a)
#     print('Nghiệm kép: X = ', x)
#     
# elif delta < 0:
#     print('Vô nghiệm')
#     
# else:
#     x1 = (-b+delta**0.5)/(2*a)
#     x2 = (-b-delta**0.5)/(2*a)
#     print('X1 = ', x1)
#     print('X2 = ', x2)
    
    
# Tính n!

# def giai_thua(n):
#     
#     gt = 1
#     
#     for i in range(2, n+1):
#         gt = gt * i
#     return gt
# 
# 
# a = int(input('Nhập giá trị của n: '))
# print('N! =', giai_thua(a))