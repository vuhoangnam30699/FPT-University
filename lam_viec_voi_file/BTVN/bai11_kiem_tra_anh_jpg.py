"""

Ảnh jpg là một tập tin nhị phân có đặc điểm là 4 byte
dữ liệu từ vị trí thứ 6 đến thứ 9 tạo thành chữ JFIF
(vị trí bắt đầu tính từ số 0). Hãy nhập tên tập tin, kiểm
tra xem đó có thể là tập tin ảnh jpg không?

"""


def kiem_tra_anh_jpg(ten_file):
    try:
        
        with open(ten_file, 'rb') as f:
            
            f.seek(6)
            
            
            data = f.read(4)
            
            
            if data == b'JFIF':
                print(f"Tập tin '{ten_file}' CHÍNH XÁC là tập tin ảnh JPEG (định dạng JFIF).")
            else:
                print(f"Tập tin '{ten_file}' KHÔNG PHẢI là tập tin ảnh JPEG định dạng JFIF.")
                
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tập tin '{ten_file}'.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


ten = input("Nhập tên tập tin cần kiểm tra: ")
kiem_tra_anh_jpg(ten)