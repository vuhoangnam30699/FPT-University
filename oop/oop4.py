class Student:
    def __init__(self,
                 student_name: str,
                 student_class: str,
                 assignment: float,
                 practical_exam: float,
                 final_exam: float
                 ):
        
        self._name = student_name
        self._class = student_class
        self._assignment = float(assignment)
        self._practical_exam = float(practical_exam)
        self._final_exam = float(final_exam)
        
    def get_name(self):
        return self._name
        
    
    def display_info(self):
        print(f"Name: {self._name}")
        print(f"Class: {self._class}")
        print(f"Assignment: {self._assignment}")
        print(f"Practical Exam: {self._practical_exam}")
        print(f"Final Exam: {self._final_exam}\n")
        
        
database = []

while True:
    print("\n----- STUDENT MANAGEMENT SYSTEM -----")
    print("1. New (Add & Display current list)")
    print("2. Display & Sort by Name (A -> Z)")
    print("3. Exit")
    
    choice = input("Please select a function (1-3): ").strip()
    print("-" * 30)
    
    if choice == "1":
        print(">> NEW <<")
        student_name = input("Name: ").strip()
        student_class = input("Class: ").strip()
        
        try:
            assignment = input("Assignment: ")
            practical_exam = input("Practical Exam: ")
            final_exam = input("Final Exam: ")
            
            student = Student(student_name, student_class, assignment, practical_exam, final_exam)
            database.append(student)
            print("\n=> Added successfully!")
        except ValueError:
            print("\n[Error] Marks must be numbers!")
        
    elif choice == "2":
        print(">> DISPLAY & SORT BY NAME (A -> Z) <<")
        if not database:
            print("Database is empty!")
        else:
            database.sort(key=lambda s: s.get_name().split()[-1].lower())
            
            for index, student in enumerate(database, 1):
                print(f"{index}. ", end="")
                student.display_info()
                
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

    