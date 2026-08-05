"""

Đọc 1 file và in ra màn hình 5 dòng đầu tiên, nếu file
không đủ 5 dòng thì in toàn bộ nội dung file.

"""


f = open("test.txt", "r", encoding = "utf-8")
count = 0
for line in f:
    line = line.strip()
    print(line)
    count += 1
    if count == 5:
        break
    
f.close()