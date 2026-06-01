""" 1. Người dùng nhập từ bàn phím liên tiếp các từ tiếng Anh viết tách nhau bởi dấu cách.
Hãy nhập chuỗi đầu vào và tách thành các từ sau đó in ra màn hình các từ
đó theo thứ tự từ điển.

"""

a = input('Nhập chuỗi tiếng Anh: ')

b = a.split()

b.sort(key = str.lower)

print(b)

