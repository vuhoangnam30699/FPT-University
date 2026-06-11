class TriangleError(ValueError):
    pass

class PositiveIntegerError(ValueError):
    pass


def validate_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise PositiveIntegerError("Lỗi: Vui lòng nhập a, b, c lớn hơn 0")
    if a + b <= c or a + c <= b or b + c <= a:
        raise TriangleError("Lỗi: Ba cạnh không thể tạo thành một tam giác")


while True:
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        c = int(input("c = "))

        validate_triangle(a, b, c)
        print("OK!")
        break
        # if a > 0 and b > 0 and c > 0:
        #     if a + b > c and a + c > b and b + c > a:
        #         print("Tam giác hợp lệ.")
        #         break
        #     else:
        #         raise ValueError("Lỗi: Ba cạnh không thể tạo thành một tam giác.")
        # if a <= 0 or b <= 0 or c <= 0:
        #     raise ValueError("Lỗi: Vui lòng nhập a, b, c lớn hơn 0.")
        
        # if a != int(a) or b != int(b) or c != int(c):
        #     raise ValueError("Lỗi: Vui lòng nhập số nguyên.")
    # except ValueError as e:
    #    print(e)

    except (TriangleError, PositiveIntegerError) as e:
        print(e)
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên")