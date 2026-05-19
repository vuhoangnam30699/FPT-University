def tich(a, b):
    return a * b


# dt = tich(100, 200)
# s = tich(20, 30) + tich(40, 50)
# 
# print(dt)
# print(s)

if __name__ == "__main__":
    print("This is the main module")
    
    dt = tich(100, 200)
    print(dt)
    
    s = tich(20, 30) + tich(40, 50)
    print(s)
    
# tham số tùy biến    
def sayHello(*names):
    #duyệt các tham số
    for name in names:
        print("Hello", name)
        
# gọi hàm với nhiều (3) tham số
sayHello("Nam1", "Nam2", "Nam3")

# gọi hàm với nhiều (2) tham số
sayHello("Nam4", "Nam5")


def sendMessage(x):
    
    
    if x == 0:
        print('Chưa gửi được')
    elif x == 1:
        print('Đã gửi')
    elif x == 2:
        print('Đã đọc')
    else:
        print('Vui lòng chỉ nhập số 0, 1, 2 hoặc chữ E để thoát')
        
        

# user_input = int(input('Vui lòng nhập x [0, 1, 2]: '))
# sendMessage(user_input)


# Vòng lặpe để chương trình chạy liên tục đến khi được yêu cầu dừng lại
while True:
    print("\n--- Chương trình đang chạy ---")
    print("Nhập số 0, 1, 2 để lưu tình trạng")
    print("Nhập E để thoát chương trình.")

    
    user_input = input('Nhập: ')

    # Kiểm tra điều kiện dừng (Cho phép dừng khi người dùng nhập 'q')
    if user_input.lower() == 'e':
        print("Đang đóng chương trình... Tạm biệt!")
        break  # Thoát chương trình


    # try-catch
    try:
        value = int(user_input)
        sendMessage(value)
    except ValueError:
         print("Vui lòng chỉ nhập số 0, 1, 2 hoặc chữ E để thoát")


    


    
    







        