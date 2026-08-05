import math
class Main:
    #====================f1====================
    def f1(self, num):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        try:
            num = int(num)
            if num <= 0:
                print(0)
                return
                
            total_sum = 0.0
            for i in range(1, num + 1):
                term = 1 / math.factorial(i)
                if i % 2 == 0:
                    total_sum -= term
                else:
                    total_sum += term
                    
            print(total_sum)
        except (ValueError, TypeError, OverflowError):
            pass
        # ===END DEF
    
    #====================f1====================
    def f2(self, row):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        try:
            row = int(row)
            for i in range(row):
                line = []
                for j in range(row - i):
                    if i == 0 or j == 0 or j == row - i - 1:
                        line.append(chr(65 + j))
                    else:
                        line.append(" ")
                print(" ".join(line))
        except (ValueError, TypeError):
            pass
        # ===END DEF

    #====================f2====================
    def f3(self, Str):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        try:
            Str = str(Str)
            seen = set()
            result = []
            for char in Str:
                if char not in seen:
                    seen.add(char)
                    result.append(char)
            
            print("".join(result))
        except Exception:
            pass
        # ===END DEF   

#================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" Your selection (1 -> 3): ")
        choice = int(input())
        if choice == 1:
            num = int(input("Enter the number of terms: "))
            print("OUTPUT")
            self.f1(num)
        elif choice == 2:
            row = int(input("Enter the number of rows: "))
            print("OUTPUT")
            self.f2(row)
        elif choice == 3:
            Str = input("Enter a string: ")
            print("OUTPUT")
            self.f3(Str)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()





