# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========
class Book:
    def __init__(self, name="", year=0, doi=""):
        self.name = name
        self.year = year
        self.doi = doi

    def display(self, index):
        print(f"Book {index}")
        print(self.name)
        print(self.year)
        print(self.doi)

class Novel(Book):
    def __init__(self, name="", year=0, doi="", author=""):
        super().__init__(name, year, doi)
        self.__author = author

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print(f"Year: {self.year}")
        print(f"DOI: {self.doi}")
        print(f"Name: {self.name}")
        print(f"Author: {self.__author}")
#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST BOOKS========
    def InputListBook(self):
        try:
            n_str = input('Enter the number of books: ')
            n = int(n_str)
            books = []
            for i in range(1, n + 1):
                print(f"Enter book {i}")
                name = input("Enter name : ")
                year = int(input("Enter year : "))
                doi = input("Enter doi : ")
                books.append(Book(name, year, doi))
            return books
        except Exception:
            return []
        # ===END DEF
    def InputNovel(self):
        try:
            name = input("Enter name : ")
            year = int(input("Enter year : "))
            doi = input("Enter doi : ")
            author = input("Enter author : ")
            return Novel(name, year, doi, author)
        except Exception:
            return None
        # ===END DEF

    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        bookList = self.InputListBook()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        try:
            for idx, book in enumerate(bookList, start=1):
                book.display(idx)
        except Exception:
            pass   
        # ===END DEF
    #==========================================

    #====================f2====================
    def f2(self):
        #=======DO NOT EDIT CODE BELOW===============
        bookList = self.InputListBook()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        try:
            bookList.sort(key=lambda x: x.name)
            for idx, book in enumerate(bookList, start=1):
                book.display(idx)
        except Exception:
            pass
        # ===END DEF
    #==========================================



    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        bookList = self.InputListBook()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        try:
            filtered_books = [b for b in bookList if b.doi.startswith("10.1000")]
            
            filtered_books.sort(key=lambda x: x.year, reverse=True)
            
            for idx, book in enumerate(filtered_books, start=1):
                book.display(idx)
        except Exception:
            pass
        # ===END DEF
    #==========================================
    
    def f4(self):
        # =======DO NOT EDIT CODE BELOW===============
        nov = self.InputNovel()
        print("OUTPUT")
        # ==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        try:
            if nov is not None:
                nov.display_info()
        except Exception:
            pass
        # ===END DEF  



#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" 4. Test f4 (1 mark)")
        print(" Your selection (1 -> 4): ")
        choice = int(input())
        
        if choice == 1:
            self.f1()
        elif choice == 2:
            self.f2()
        elif choice == 3:
            self.f3()
        elif choice == 4:
            self.f4()
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()
