"""

Đọc tập tin văn bản abc.txt sau đó chuyển nội dung
đọc được sang chữ in hoa và ghi vào tập tin xyz.txt

"""


def chuyen_doi_in_hoa(file_nguon, file_dich):
    try:
        # Mở song song cả 2 file: 
        # - file_nguon để đọc ('r')
        # - file_dich để ghi ('w') -> Nếu file xyz.txt chưa có, Python sẽ tự tạo mới
        with open(file_nguon, 'r', encoding='utf-8') as f_vao, \
             open(file_dich, 'w', encoding='utf-8') as f_ra:
            
            # Duyệt qua từng dòng trong file nguồn
            for dong in f_vao:
                # Chuyển dòng đó thành chữ in hoa
                dong_in_hoa = dong.upper()
                
                # Ghi dòng đã in hoa vào file đích
                f_ra.write(dong_in_hoa)
                
        print(f"Đã chuyển đổi thành công! Vui lòng kiểm tra file '{file_dich}'.")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file nguồn '{file_nguon}'. Vui lòng tạo file này trước.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


chuyen_doi_in_hoa('abc.txt', 'xyz.txt')