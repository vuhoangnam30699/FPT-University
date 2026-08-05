"""

Đọc tập tin văn bản abc.txt sau đó chuyển nội dung
đọc được sang chữ in hoa và ghi vào tập tin xyz.txt

"""


def chuyen_doi_in_hoa(file_nguon, file_dich):
    try:
        
        with open(file_nguon, 'r', encoding='utf-8') as f_vao, \
             open(file_dich, 'w', encoding='utf-8') as f_ra:
            
            
            for dong in f_vao:
                
                dong_in_hoa = dong.upper()
                
                
                f_ra.write(dong_in_hoa)
                
        print(f"Đã chuyển đổi thành công! Vui lòng kiểm tra file '{file_dich}'.")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file nguồn '{file_nguon}'. Vui lòng tạo file này trước.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


chuyen_doi_in_hoa('abc.txt', 'xyz.txt')