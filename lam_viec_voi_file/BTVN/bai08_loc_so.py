"""

Đọc tập tin văn bản abc.txt, lọc lấy tất cả các số trong
dữ liệu đọc được và ghi chúng lần lượt vào tập tin
number.txt, mỗi số ghi trên một dòng

"""


def loc_va_ghi_so(file_nguon, file_dich):
    try:
        with open(file_nguon, 'r', encoding='utf-8') as f_vao, \
             open(file_dich, 'w', encoding='utf-8') as f_ra:
            
            for dong in f_vao:
                so_hien_tai = ""
                
                for ky_tu in dong:
                    if ky_tu.isdigit():
                        so_hien_tai += ky_tu
                    else:
                        if so_hien_tai:
                            f_ra.write(so_hien_tai + '\n')
                            so_hien_tai = ""
                
                if so_hien_tai:
                    f_ra.write(so_hien_tai + '\n')
                    
        print(f"Đã lọc xong! Các số đã được ghi vào file '{file_dich}', mỗi số một dòng.")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file nguồn '{file_nguon}'.")


loc_va_ghi_so('abc.txt', 'number.txt')