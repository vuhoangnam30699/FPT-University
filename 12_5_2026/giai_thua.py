# Tính n!

def giai_thua(n):
    
    gt = 1
    
    for i in range(2, n+1):
        gt = gt * i
    return gt


a = int(input('Nhập giá trị của n: '))
print('N! =', giai_thua(a))