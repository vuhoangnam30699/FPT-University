while True:
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        fraction = a / b
        print(f"a/b =", fraction)
        break
    except ValueError:
        print("Vui lòng nhập số nguyên")
    except ZeroDivisionError:
        print("b không được bằng 0.")