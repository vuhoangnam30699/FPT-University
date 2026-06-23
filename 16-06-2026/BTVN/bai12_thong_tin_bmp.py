"""

Ảnh bitmap (BMP) là một tập tin nhị phân:
- 2 byte đầu tạo nên chữ BM
- 4 byte từ vị trí 18-21 tạo nên số nguyên 4 byte là số
dòng (chiều cao) của ảnh
- 4 byte từ vị trí 22-25 tạo nên số nguyên 4 byte là số
cột (chiều ngang) của ảnh
Nhập tên tập tin, cho biết đó có phải là ảnh bitmap
không, nếu đúng thì in ra cỡ của ảnh (dòng x cột)

"""


import struct

def thong_tin_anh_bmp(ten_file):
    try:
        with open(ten_file, 'rb') as f:
            # 1. Kiểm tra 2 byte đầu tiên
            header = f.read(2)
            if header != b'BM':
                print(f"Tập tin '{ten_file}' không phải là ảnh BMP.")
                return

            # 2. Đọc chiều cao (vị trí 18-21) và chiều ngang (vị trí 22-25)
            # Di chuyển con trỏ đến vị trí 18
            f.seek(18)
            
            # Đọc 4 byte cho chiều ngang (width) và 4 byte cho chiều cao (height)
            width_bytes = f.read(4)
            height_bytes = f.read(4)
            
            # Sử dụng struct.unpack để chuyển byte sang số nguyên
            # '<i' nghĩa là: Little-endian (định dạng chuẩn của BMP) và kiểu số nguyên (integer)
            width = struct.unpack('<i', width_bytes)[0]
            height = struct.unpack('<i', height_bytes)[0]
            
            # Lưu ý: Trong BMP, chiều cao thường lưu giá trị âm nếu ảnh lưu từ trên xuống dưới, 
            # nên ta lấy giá trị tuyệt đối.
            print(f"Đây là ảnh BMP.")
            print(f"Kích thước ảnh: {abs(height)} dòng x {width} cột.")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tập tin '{ten_file}'.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# --- Thực thi ---
ten = input("Nhập tên tập tin ảnh BMP: ")
thong_tin_anh_bmp(ten)