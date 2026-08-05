""" 													"xử lý” ngoại lệ											"""

while True:  # Tạo một vòng lặp vô hạn để ép người dùng phải nhập đúng mới thoát

    try:
        # Khối lệnh try: Nơi chứa đoạn code "có thể" gây ra lỗi
        x = int(input("Nhập số X: "))
        
        # Nếu dòng trên chạy mượt mà (người dùng nhập số), dòng break dưới đây sẽ được thực thi
        break  # Thoát khỏi vòng lặp while khi đã nhập đúng

    except ValueError:
        # Khối lệnh except ValueError: "Bắt" riêng lỗi ValueError
        # Lỗi này xảy ra khi hàm int() không thể chuyển đổi chuỗi thành số (VD: nhập chữ "abc")
        
        # Nếu có lỗi ValueError xảy ra trong khối try, Python sẽ LẬP TỨC dừng khối try lại,
        # nhảy xuống đây và chạy các lệnh trong khối except này thay vì làm sập chương trình.
        print("Lỗi, hãy nhập lại.")
        
        # Sau khi chạy xong khối except này, vòng lặp while True lại tiếp tục quay vòng mới.

print("X=", x)


"""												Cú pháp try-except-else-finally

· Cú pháp:	try:
            except:
            else:
            finally:
            
· Công việc của từng khối:
    - Khối “try”: đoạn mã có khả năng gây lỗi, khi lỗi xảy ra, khối này sẽ bị dừng ở dòng gây lỗi
    - Khối “except”: đoạn mã xử lý lỗi, chỉ thực hiện nếu có lỗi xảy ra
    - Khối "else”: có thể xuất hiện ngay sau khối except cuối cùng, đoạn mã sẽ được thực hiện nếu không có except nào được
        thực hiện (đoạn try không có lỗi)
    - Khối “finally": còn được gọi là khối clean-up, luôn được thực hiện dù có xảy ra lỗi hay không
    
· Chú ý:
    - Khối try chỉ có 1 khối duy nhất, phải viết đầu tiên
    - Khối finally có thể có hay không, nếu có thì khối này phải viết cuối cùng
    - Khối except có thể không viết, có một khối, hoặc nhiều khối except khác nhau (để xử lý nhiều tình huống lỗi khác nhau)
    - Một khối except có thể xử lý một loại lỗi, nhiều loại lỗi hoặc tất cả các loại lỗi
    - Nếu không xử lý triệt để lỗi có thể “ném” trả lại lỗi này bằng lệnh “raise"
    - Có thể phát sinh một ngoại lệ bằng lệnh "raise <lỗi>"
    - Khi lỗi xảy ra, một biến chứa lỗi được phát sinh và “ném" xuống phần các khối except, khối except
        đầu tiên “bắt” được ngoại lệ sẽ xử lý nó

"""


"""										Quy tắc “bắt” ngoại lệ: lọt sàng xuống nia						"""

except (NameError, TypeError) :						# xử lý 2 loại lỗi
    print("Name or Type error")						# lấy biến lỗi, đặt tên là e
except IOError as e:
    print(e)
    raise											# "ném" trả lại lỗi này
except ValueError:									# xử lý lỗi Value
    print("Value error")
except:												# xử lý mọi lỗi khác
    print("An error occurred")
    raise NameError("Ko biet")						# tạo ra một lỗi "Ko biet”
else:												# thực hiện nếu không có lỗi
    print("OK")
    
    
""" Tự sinh lỗi """


"""
Từ khóa raise

· Python cung cấp từ khóa raise sử dụng khi cần phát sinh một ngoại lệ
    - Nếu chỉ viết "raise": cách viết này chỉ đúng trong khối except, khi ta không xử lý được ngoại lệ hiện tại và
        “ném trả” ngoại lệ về cho chương trình cha
    - Nếu viết “raise <biến>”: phát sinh một ngoại lệ và <biến> sẽ chứa các thông tin báo lỗi về ngoại lệ xảy ra
        + Trong trường hợp này, <biến> nên có kiểu Exception hoặc kế thừa từ Exception, kiểu càng cụ thể thì
            càng cung cấp nhiều thông tin cho quá trình sửa lỗi
    - Lập trình viên có thể tạo một kiểu ngoại lệ mới

"""


""" Ví dụ về phát sinh ngoại lệ """

try:
    a = int(input("Nhập một số nguyên dương nhỏ hơn 100: "))
    # sinh lỗi khi số quá bé
    if a <= 0:
        raise ValueError("Bạn đã nhập một số quá nhỏ")
    # sinh lỗi khi số quá lớn
    if a >= 100:
        raise ValueError("Bạn cần nhập số nhỏ hơn 100")
# bắt lỗi:
# - nhập không phải số nguyên
# - nhập số quá lớn
# - nhập số quá bé
except ValueError as ex:
    print(ex)








