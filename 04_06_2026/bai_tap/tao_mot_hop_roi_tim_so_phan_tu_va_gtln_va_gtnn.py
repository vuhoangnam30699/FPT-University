"""

Tạo một tập hợp gồm các số nhập vào từ bàn phím
(nhập trên 1 dòng, cách nhau bởi ký tự trống), tìm và
in ra số phần tử của tập, giá trị lớn nhất và nhỏ nhất
trong tập

"""


cac_so = input('Nhap so di (dung co nhap chu): ')

tap_hop = {int(x) for x in cac_so.split()}

if tap_hop:
    
    so_phan_tu = len(tap_hop)
    gtln = max(tap_hop)
    gtnn = min(tap_hop)
    
    print('Tap hop: ', tap_hop)
    print('So phan tu: ', so_phan_tu)
    print('GTLN: ', gtln)
    print('GTNN: ', gtnn)
    
else:
    print('N/A')
    

