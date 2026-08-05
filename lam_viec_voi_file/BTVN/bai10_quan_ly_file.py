"""

Lấy danh sách các tập tin trong thư mục hiện tại, tiến
hành so sánh nội dung của các tập tin trong thư mục,
và chỉ ra cac tap tin co nội dung giong nhau. Chưong
trình in ra các nhóm tập tin có cùng nội dung, đánh số
các nhóm tăng dần bắt đầu từ 1

"""


import os

def tim_cac_file_giong_nhau():
    
    file_groups = {}
    
    file_list = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    for filename in file_list:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if content in file_groups:
                file_groups[content].append(filename)
            else:
                file_groups[content] = [filename]
        except Exception:
            continue

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