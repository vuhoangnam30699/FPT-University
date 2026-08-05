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
            
            header = f.read(2)
            if header != b'BM':
                print(f"Tập tin '{ten_file}' không phải là ảnh BMP.")
                return

            
            f.seek(18)
            
            
            width_bytes = f.read(4)
            height_bytes = f.read(4)
            
            
            width = struct.unpack('<i', width_bytes)[0]
            height = struct.unpack('<i', height_bytes)[0]
            
            
            print(f"Đây là ảnh BMP.")
            print(f"Kích thước ảnh: {abs(height)} x {width}")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tập tin '{ten_file}'.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


ten = input("Nhập tên tập tin ảnh BMP: ")
thong_tin_anh_bmp(ten)