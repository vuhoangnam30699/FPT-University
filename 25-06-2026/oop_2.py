class Person:
    person_id = 0
    
    def __init__(self, person_name: str, person_age: int):
        Person.person_id += 1
        self._id = Person.person_id
        self._name = person_name
        self._age = person_age

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name
    
    def set_name(self, person_name: str):
        self._name = person_name

    def get_age(self) -> int:
        return self._age
    
    def set_age(self, person_age: int):
        if person_age < 18:
            raise ValueError("Tuổi phải từ 18 trở lên!")
        self._age = person_age

    def display_info(self):
        print(f"ID: {self.get_id()}")
        print(f"Tên: {self.get_name()}")
        print(f"Tuổi: {self.get_age()}")


class Subject:
    def __init__(self, credit_name: str, first_score: float, second_score: float):
        self._credit_name = credit_name
        self._first_score = first_score
        self._second_score = second_score

    def get_credit_name(self) -> str:
        return self._credit_name

    def get_first_score(self) -> float:
        return self._first_score

    def get_second_score(self) -> float:
        return self._second_score


class Student(Person):
    def __init__(self, person_name: str, person_age: int, student_code: str):
        super().__init__(person_name, person_age)
        self._student_code = student_code
        self._subjects = []
        
    def get_student_code(self) -> str:
        return self._student_code
    
    def set_student_code(self, student_code: str):
        self._student_code = student_code

    def get_subjects(self) -> list:
        return self._subjects

    def has_subject(self, subject_name: str) -> bool:
        return any(sub.get_credit_name().lower() == subject_name.lower() for sub in self._subjects)

    def add_subject(self, subject: Subject):
        if self.has_subject(subject.get_credit_name()):
            raise ValueError(f"Sinh viên đã học môn '{subject.get_credit_name()}' này rồi!")
        self._subjects.append(subject)
        
    def display_info(self):
        super().display_info()
        print(f"MSSV: {self.get_student_code()}")
        print("Danh sách môn học:")
        if not self._subjects:
            print("  (Chưa đăng ký môn học nào)")
        else:
            for sub in self._subjects:
                print(f"  + Môn: {sub.get_credit_name()} | Điểm L1: {sub.get_first_score()} | Điểm L2: {sub.get_second_score()}")
        print("-" * 30)


def get_int_or_q(prompt_message: str):
    while True:
        val = input(prompt_message).strip().lower()
        if val == 'q':
            return 'q'
        try:
            return int(val)
        except ValueError:
            print("Lỗi: Vui lòng nhập vào một số nguyên hoặc gõ 'Q' để quay lại!")
            

def get_float_or_q(prompt_message: str):
    while True:
        val = input(prompt_message).strip().lower()
        if val == 'q':
            return 'q'
        try:
            return float(val)
        except ValueError:
            print("Lỗi: Vui lòng nhập vào một số thập phân hoặc gõ 'Q' để quay lại!")


database = []

while True:
    print("----- HỆ THỐNG QUẢN LÝ SINH VIÊN -----")
    print("1. Nhập thông tin sinh viên mới")
    print("2. Thêm môn học và điểm cho sinh viên")
    print("3. Hiển thị danh sách sinh viên")
    print("4. Thoát chương trình")
    
    choice = input("Mời bạn chọn chức năng (1-4): ").strip()
    print("-" * 30)

    if choice == "1":
        print(">> NHẬP THÔNG TIN SINH VIÊN MỚI <<")
        print("(Nhập 'q' hoặc 'Q' bất cứ lúc nào để QUAY LẠI menu chính)\n")
        
        name = input("Tên: ").strip()
        if name.lower() == "q":
            print("=> Đã hủy thao tác thêm sinh viên.\n")
            continue
        
        student = Student(person_name=name, person_age=0, student_code="")
        
        is_back = False
        while True:
            age = get_int_or_q("Tuổi: ")
            if age == 'q':
                is_back = True
                break
            try:
                student.set_age(age)
                break 
            except ValueError as e:
                print(f"Lỗi: {e} Vui lòng nhập lại!")
        
        if is_back:
            print("=> Đã hủy thao tác thêm sinh viên.\n")
            continue

        while True:
            mssv = input("MSSV: ").strip()
            if mssv.lower() == "q":
                is_back = True
                break
            if not mssv:
                print("Lỗi: MSSV không được để trống!")
                continue
                
            is_duplicate = any(s.get_student_code() == mssv for s in database)
            if is_duplicate:
                print(f"Lỗi: MSSV '{mssv}' đã tồn tại! Vui lòng nhập mã khác.")
            else:
                student.set_student_code(mssv)
                break
                
        if is_back:
            print("=> Đã hủy thao tác thêm sinh viên.\n")
            continue
        
        database.append(student)
        print("=> Thêm thông tin sinh viên thành công!\n")

    elif choice == "2":
        print(">> THÊM MÔN HỌC VÀ NHẬP ĐIỂM <<")
        if not database:
            print("Danh sách trống! Không có sinh viên để thêm môn.\n")
            continue
            
        print("--- DANH SÁCH MSSV TRÊN HỆ THỐNG GỢI Ý ---")
        for i, s in enumerate(database, 1):
            print(f" {i}. MSSV: {s.get_student_code()} | Tên: {s.get_name()}")
        print("-" * 40)
        print("(Nhập 'q' hoặc 'Q' để QUAY LẠI menu chính)\n")
        
        found_student = None
        while True:
            search_code = input("Nhập đúng MSSV từ danh sách trên: ").strip()
            if search_code.lower() == "q":
                break
            
            found_student = next((s for s in database if s.get_student_code() == search_code), None)
            if found_student is not None:
                break
            else:
                print("Lỗi: MSSV không tồn tại trong danh sách gợi ý! Vui lòng nhập lại.")
        
        if search_code.lower() == "q":
            print("=> Đã quay lại menu chính.\n")
            continue

        print(f"\n=> Đang thêm môn học cho sinh viên: {found_student.get_name()}")
        credit_name = input("Nhập tên môn học mới: ").strip()
        if credit_name.lower() == "q" or not credit_name:
            print("=> Đã hủy thao tác thêm môn học.\n")
            continue
            
        if found_student.has_subject(credit_name):
            print(f"Lỗi: Sinh viên này đã học môn '{credit_name}' rồi!\n")
            continue
        
        is_back = False
        while True:
            score1 = get_float_or_q("Nhập điểm lần 1: ")
            if score1 == 'q':
                is_back = True
                break
            if 0 <= score1 <= 10:
                break
            print("Lỗi: Điểm phải nằm trong khoảng từ 0 đến 10!")
                
        if is_back:
            print("=> Đã hủy thao tác thêm môn học.\n")
            continue
        
        while True:
            score2 = get_float_or_q("Nhập điểm lần 2: ")
            if score2 == 'q':
                is_back = True
                break
            if 0 <= score2 <= 10:
                break
            print("Lỗi: Điểm phải nằm trong khoảng từ 0 đến 10!")
                
        if is_back:
            print("=> Đã hủy thao tác thêm môn học.\n")
            continue
                
        
        new_subject = Subject(credit_name=credit_name, first_score=score1, second_score=score2)
        found_student.add_subject(new_subject)
        print(f"=> Thêm môn '{credit_name}' cùng điểm số thành công!\n")

    elif choice == "3":
        print(">> DANH SÁCH SINH VIÊN VÀ MÔN HỌC <<")
        if not database:
            print("Danh sách trống!\n")
        else:
            for member in database:
                member.display_info()
        input("Ấn Enter để quay lại menu chính...")
        print()
 
    elif choice == "4":
        while True:
            confirm = input("Bạn có chắc chắn muốn thoát chương trình không? (y/n): ").strip().lower()
            if confirm == 'y':
                print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
                break
            elif confirm == 'n':
                print("Đã hủy thao tác thoát. Quay lại menu chính.\n")
                break
            else:
                print("Lỗi: Vui lòng chỉ nhập 'y' (Yes) hoặc 'n' (No)!")
        
        if confirm == 'y':
            break
        
    else:
        print("Lựa chọn không hợp lệ! Vui lòng chọn lại từ 1 đến 4.\n")