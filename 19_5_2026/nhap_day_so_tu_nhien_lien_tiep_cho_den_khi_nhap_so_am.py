"""

Viết chương trình cho phép người dùng nhập vào liên
tiếp một dãy số tự nhiên (không biết trước độ dài),
việc nhập dãy sẽ kết thúc khi người dùng nhập một số
âm nào đó

"""

list_number = []

print("Nhập vào các số tự nhiên (Nhập một số âm để kết thúc):")
while True:
    number = int(input("Nhập số: "))
    
    if number < 0:
        print("Đã nhận diện số âm. Dừng nhập!")
        break
        
    list_number.append(number)

print("Dãy số tự nhiên bạn đã nhập là:", list_number)