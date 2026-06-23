"""

Đọc 1 file, tìm và in ra nội dung của dòng dài nhất
trong file đó

"""


longest_line = ""
max_length = 0

try:
    with open("test.txt", "r", encoding = "utf-8") as f:
        for line in f:
            # Loại bỏ ký tự xuống dòng (\n) ở cuối mỗi dòng trước khi đo độ dài
            each_line = line.strip('\n')
            
            # Nếu tìm thấy dòng có độ dài lớn hơn độ dài lớn nhất hiện tại
            if len(each_line) > max_length:
                max_length = len(each_line)
                longest_line = each_line
                
    # Kiểm tra xem file có nội dung hay không
    if max_length > 0:
        print(longest_line)
    else:
        print("N/A")
except FileNotFoundError:
    print("File not found!")
            
            