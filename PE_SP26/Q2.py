import math
class Main:
    #====================f1====================
    def f1(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        try:
            with open(fileName, 'r') as f:
                content = f.read().split()
                for token in content:
                    print(token)
        except FileNotFoundError:
            pass
        # ===END DEF

    #====================f2====================
    def f2(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        try:
            with open(fileName, 'r') as f:
                content = f.read().split()
                
                numbers = [int(x) for x in content]
                
                prime_numbers = []
                for num in numbers:
                    if num < 2:
                        continue
                    
                    is_prime = True
                    for i in range(2, int(math.sqrt(num)) + 1):
                        if num % i == 0:
                            is_prime = False
                            break
                            
                    if is_prime:
                        prime_numbers.append(num)
                
                prime_numbers.sort()
                print(prime_numbers)
                
        except FileNotFoundError:
            pass
        # ===END DEF   
        
#====================DO NOT CHANGE THE CODE BELOW====================================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (2 mark)")
        print(" Your selection (1 -> 2): ")
        choice = int(input())
        fileName = input()
        print("OUTPUT")
        if choice == 1:
            self.f1(fileName)
        elif choice == 2:
            self.f2(fileName)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()
