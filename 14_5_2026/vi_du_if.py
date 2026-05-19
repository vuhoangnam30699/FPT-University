age = int(input("Bạn bao nhiêu tuối? "))
print("Ò bạn đã", age, "tuổi rồi!")
if age >= 18:
    print("Đủ tuổi đi bầu cử")
    if age > 100:
        print("Có vẻ sai sai!")
else:
    print("Nhỏ quá")