class Person:
    person_id = 0
    
    def __init__(self,
                 person_name: str,
                 person_age: int,
                 #role: str
                 ):
        
        Person.person_id += 1
        
        self.id = Person.person_id
        self.name = person_name
        self.age = person_age
        #self.role = role

    def display_info(self):
        #print(f"[{self.role}]")
        print(f"ID: {self.id}")
        print(f"Tên: {self.name}")
        print(f"Tuổi: {self.age}")
        
        
        
class Student(Person):
    
    def __init__(self,
                 person_name: str,
                 person_age: int,
                 student_code: str,
                 credit: str,
                 first_score: float,
                 second_score: float
                 ):
#         super().__init__(person_name, person_age, role="Student")
        super().__init__(person_name, person_age)
        self.student_code = student_code
        self.credit = credit
        self.first_score = first_score
        self.second_score = second_score
        
    def display_info(self):
        super().display_info()
        print(f"MSSV: {self.student_code}")
        print(f"Môn học: {self.credit}")
        print(f"Điểm lần 1: {self.first_score}")
        print(f"Điểm lần 2: {self.second_score}\n")
        
        
# class Teacher(Person):
#     
#     def __init__(self, person_name: str, person_age: int, degree: str, exp: int):
#         super().__init__(person_name, person_age, role="Teacher")
#         self.degree = degree
#         self.exp = exp
#         
#     def display_info(self):
#         super().display_info()
#         print(f"Degree: {self.degree}")
#         print(f"Experience: {self.exp}\n")
        


# s1 = Student("S1", 20, "FPTU", 3)
# s2 = Student("S2", 19, "VNU", 2)
# t1 = Teacher("T1", 28, "Bachelor", 5)
# t2 = Teacher("T2", 40, "Master", 12)
# 
# 
# s1.display_info()
# s2.display_info()
# t1.display_info()
# t2.display_info()


# ==========================================================
# CÁC HÀM TIỆN ÍCH BẮT NHẬP LẠI TẠI CHỖ (VALIDATION FUNCTIONS)
# ==========================================================

# Yêu cầu nhập số nguyên, sai bắt nhập lại ngay tại chỗ
def get_int_input(prompt_message: str) -> int:
    while True:
        try:
            return int(input(prompt_message))
        except ValueError:
            print("Lỗi: Vui lòng nhập vào một số nguyên hợp lệ!")
            

# Yêu cầu nhập số thực (thập phân), sai bắt nhập lại ngay tại chỗ
def get_float_input(prompt_message: str) -> float:
    while True:
        try:
            return float(input(prompt_message))
        except ValueError:
            print("Lỗi: Vui lòng nhập vào một số thập phân hợp lệ (Ví dụ: 3.5)!")

# Hiển thị menu nhỏ để chọn bằng cấp nhanh chóng
# def get_degree_input() -> str:
#     while True:
#         print("Chọn bằng cấp:")
#         print("  1. Cử nhân")
#         print("  2. Thạc sĩ")
#         print("  3. Tiến sĩ")
#         
#         choice = input("Mời bạn chọn (1-3): ").strip()
#         
#         if choice == "1":
#             return "Cử nhân"
#         elif choice == "2":
#             return "Thạc sĩ"
#         elif choice == "3":
#             return "Tiến sĩ"
#         else:
#             print("Lựa chọn không hợp lệ! Vui lòng chỉ bấm 1, 2 hoặc 3.\n")


# ==========================================================
# CHƯƠNG TRÌNH CHÍNH (MENU NHẬP LIỆU VÀ RẼ NHÁNH)
# ==========================================================

database = []

while True:
    print("----- HỆ THỐNG QUẢN LÝ -----")
#    print("1. Nhập thông tin Học sinh (Student)")
    print("1. Nhập thông tin học sinh")
#    print("2. Nhập thông tin Giáo viên (Teacher)")
    print("2. Hiển thị danh sách đã nhập")
    print("3. Thoát chương trình")
    
    choice = input("Mời bạn chọn chức năng (1-3): ").strip()
    print("-" * 30)

    if choice == "1":
        print(">> NHẬP THÔNG TIN HỌC SINH <<")
        name = input("Tên: ")
        age = get_int_input("Tuổi: ")
        mssv = input("MSSV: ")
        credit = input("Môn học: ")
        first_score = get_float_input("Điểm lần 1: ")
        second_score = get_float_input("Điểm lần 2: ")
        
        # Khởi tạo Student (ID tự tăng ngầm bên trong)
        student = Student(person_name=name,
                          person_age=age,
                          student_code=mssv,
                          credit=credit,
                          first_score=first_score,
                          second_score=second_score
                          )
        database.append(student)
        print("=> Thêm học sinh thành công!\n")

#     elif choice == "2":
#         print(">> NHẬP THÔNG TIN GIÁO VIÊN <<")
#         name = input("Nhập tên: ")
#         age = get_int_input("Nhập tuổi: ")
#         degree = get_degree_input()
#         exp = get_int_input("Nhập số năm kinh nghiệm: ")
#         
#         # Khởi tạo Teacher (ID tự tăng ngầm bên trong)
#         teacher = Teacher(person_name=name, person_age=age, degree=degree, exp=exp)
#         database.append(teacher)
#         print("=> Thêm giáo viên thành công!\n")

    elif choice == "2":
        print(">> DANH SÁCH HIỆN TẠI <<")
        if not database:
            print("Danh sách trống!\n")
        else:
            for member in database:
                # Tính đa hình (Polymorphism): Tự động gọi đúng hàm display_info của Student hoặc Teacher
                member.display_info()

    elif choice == "3":
        print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
        break
        
    else:
        print("Lựa chọn không hợp lệ! Vui lòng chọn lại từ 1 đến 3.\n")
        


    
    