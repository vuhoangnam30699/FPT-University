"""

Nhập tên của hai tập tin văn bản, đọc và so sánh xem
nội dung của hai tập tin có giống nhau hay không

"""



def so_sanh_hai_file(file1, file2):
    try:        
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
            giong_nhau = True
            
            # Sử dụng zip để duyệt song song
            for d1, d2 in zip(f1, f2):
                if d1 != d2:
                    giong_nhau = False
                    break
                
            # Kiểm tra xem file có cùng số lượng dòng không
            # Kiểm tra thêm f1 và f2 đã đọc hết chưa
            if giong_nhau:
                # Kiểm tra thêm trường hợp số dòng khác nhau
                if f1.readline() != "" or f2.readline() != "":
                    giong_nhau = False

            if giong_nhau:
                print(f"'{file1}' giống '{file2}'")
            else:
                print(f"'{file1}' khác '{file2}'")
                
    except FileNotFoundError as e:
        print(f"Lỗi: Không tìm thấy file. Chi tiết: {e}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


ten1 = input("File 1: ")
ten2 = input("File 2: ")

so_sanh_hai_file(ten1, ten2)