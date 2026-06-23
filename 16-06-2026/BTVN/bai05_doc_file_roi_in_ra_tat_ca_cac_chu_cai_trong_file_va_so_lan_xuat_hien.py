"""

Đọc 1 file, thống kê và in ra tất cả các chữ cái có trong
file và số lần xuất hiện của các chữ đó

"""


dem_chu_cai = {}

try:
    with open("test.txt", 'r', encoding='utf-8') as file:
        for dong in file:
            # Chuyển toàn bộ dòng thành chữ thường để không phân biệt 'A' và 'a'
            dong_chu_thuong = dong.lower()
                
            for ky_tu in dong_chu_thuong:
                # Kiểm tra nếu ký tự đó là chữ cái (hoặc chữ số) thì mới đếm
                # .isalnum() giúp bỏ qua khoảng trắng, dấu câu, dấu xuống dòng...
                if ky_tu.isalnum():
                    # Nếu chữ cái đã có trong dictionary, tăng số đếm lên 1
                    if ky_tu in dem_chu_cai:
                        dem_chu_cai[ky_tu] += 1
                    # Nếu chưa có, thêm chữ cái đó vào với số đếm ban đầu là 1
                    else:
                        dem_chu_cai[ky_tu] = 1

    if dem_chu_cai:
        # Sắp xếp theo thứ tự chữ cái từ A-Z
        for chu_cai in sorted(dem_chu_cai.keys()):
            print(f"Chữ cái '{chu_cai}' xuất hiện: {dem_chu_cai[chu_cai]} lần")
    else:
            print("File trống hoặc không chứa chữ cái nào.")

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file.")