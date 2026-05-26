"""

Trường hợp  một số khá lớn, không thể liệt kê được
Ta sử dụng hàm range() để tạo ra khoảng số
Dùng for để:

1. TỰ ĐỘNG HÓA HÀNH ĐỘNG: Thay thế việc gõ tay hàng nghìn dòng code lặp đi lặp lại.
2. TIẾT KIỆM BỘ NHỚ: Máy tính chạy đến đâu, hàm range() sinh số đến đó, 
   không cần lưu trữ cả triệu số cùng một lúc.
3. TỐI ƯU CODE: Xử lý lượng dữ liệu khổng lồ chỉ bằng 2 dòng lệnh gọn gàng.

"""


# In các từ 10 -> 20
for d in range(10,20):
    print(d)

# In các từ 20 -> 10, bước nhảy -1
for d in range(20, 10, -1):
    print(d)

# In các từ 1 -> 101, bước nhảy 2, là số lẻ
for d in range(1, 101, 2):
    print(d)