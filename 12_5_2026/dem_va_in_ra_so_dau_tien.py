x = int(input('Nhập X = '))
s = str(abs(x))

print('X có %d chữ số' %len(s))


chu_so_dau_tien = int(s[0])
if x < 0:
    chu_so_dau_tien = -chu_so_dau_tien

print('Chữ số đầu tiên của X:', chu_so_dau_tien)