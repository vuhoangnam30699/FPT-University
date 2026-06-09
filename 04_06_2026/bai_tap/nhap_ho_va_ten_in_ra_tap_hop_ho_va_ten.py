"""

Nhập vào từ bàn phím họ và tên đầy đủ của các sinh
viên trong lớp, mỗi người trên một dòng. Việc nhập sẽ
kết thúc khi người dùng gõ vào dòng trống. Sau đó,
hãy in ra các họ và các tên của sinh viên trong lớp

"""


cac_ten = set()
cac_ho = set()
print('Nhap ho va ten di (enter de xuong dong nhap ten khac): ')

while True:
    
    # Nhập họ và tên từ bàn phím và xóa khoảng trắng thừa
    ho_ten = input().strip()
    
    # Nếu người dùng không nhập gì mà nhấn Enter thì dừng việc nhập
    if ho_ten == "":
        break
    
    
    cac_tu = ho_ten.split()
    
    if len(cac_tu) > 0:
        ho = cac_tu[0]
        ten = cac_tu[-1]
    
    # Thêm tên vừa nhập vào tập hợp
    cac_ho.add(ho)
    cac_ten.add(ten)
    
print(cac_ho)    
print(cac_ten)
    
    
    

    