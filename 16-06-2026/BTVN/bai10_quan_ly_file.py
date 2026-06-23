"""

Lấy danh sách các tập tin trong thư mục hiện tại, tiến
hành so sánh nội dung của các tập tin trong thư mục,
và chỉ ra cac tap tin co nội dung giong nhau. Chưong
trình in ra các nhóm tập tin có cùng nội dung, đánh số
các nhóm tăng dần bắt đầu từ 1

"""


import os

def tim_cac_file_giong_nhau():
    # Dictionary để lưu nội dung file làm key, danh sách tên file làm value
    file_groups = {}
    
    # Lấy danh sách tất cả các file trong thư mục hiện tại
    file_list = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    for filename in file_list:
        try:
            # Đọc nội dung file
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Lưu vào dictionary: nếu nội dung đã tồn tại thì thêm tên file vào nhóm đó
            if content in file_groups:
                file_groups[content].append(filename)
            else:
                file_groups[content] = [filename]
        except Exception:
            # Bỏ qua các file không đọc được (như file hình ảnh, file hệ thống...)
            continue

    # Lọc và in ra các nhóm có từ 2 file trở lên
    count = 1
    
    da_co_nhom_trung = False
    for content, files in file_groups.items():
        if len(files) > 1:
            print(f"Nhóm {count}:")
            for f in files:
                print(f" - {f}")
            count += 1
            da_co_nhom_trung = True
            
    if not da_co_nhom_trung:
        print("Không tìm thấy các file có nội dung giống nhau trong thư mục này.")


tim_cac_file_giong_nhau()