"""

Đọc 1 file, tìm và in ra từ dài nhất trong file

"""


tu_dai_nhat = ""
do_dai_lon_nhat = 0

try:
    
    with open('test.txt', 'r', encoding='utf-8') as file:
        for dong in file:
            dong_chu_thuong = dong.lower()
                
            dong_lam_sach = ""
            for ky_tu in dong_chu_thuong:
                if ky_tu.isalnum() or ky_tu.isspace():
                    dong_lam_sach += ky_tu
                else:
                    dong_lam_sach += " "
                    
            cac_tu = dong_lam_sach.split()
            
            for tu in cac_tu:
                if len(tu) > do_dai_lon_nhat:
                    do_dai_lon_nhat = len(tu)
                    tu_dai_nhat = tu
                        
        if tu_dai_nhat:
            print(tu_dai_nhat)
        else:
            print("File trống hoặc không chứa từ hợp lệ.")
            
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file.")
