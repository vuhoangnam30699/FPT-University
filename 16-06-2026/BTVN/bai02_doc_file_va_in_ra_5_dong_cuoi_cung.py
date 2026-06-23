"""

Đọc 1 file và in ra màn hình 5 dòng cuối cùng, nếu file
không đủ 5 dòng thì in toàn bộ nội dung file.

"""


with open("test.txt", "r", encoding = "utf-8") as f:
    # Đọc toàn bộ các dòng vào một list
    all_lines = f.readlines()
    
    # Lấy 5 dòng cuối cùng
    last_5_lines = all_lines[-5:]
    
    # Duyệt và in ra từng dòng
    for line in last_5_lines:
        print(line.strip())
    
    
