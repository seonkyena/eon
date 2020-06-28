import os

class BuchData:
    def __init__(self):
        self.Book_lineup = []

    def buch_list(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'input.txt')
        Book_list = open(my_file,'r')
        while True:
            try:
                lostop = Book_list.readline().split()
                self.Book_lineup.append(lostop)
                if not lostop:
                    break
            except IOError:
                print('파일이 존재하지 않습니다')
        self.Book_lineup.pop(-1)
        return self.Book_lineup
        
    def plus(self):
        self.Book_in = input("도서명, 저자, 출판연도, 출판사명, 장르를 입력해주세요 : ").split()
        if len(self.Book_in) == 5:
            self.Book_lineup.append(self.Book_in)
            print("추가되었습니다. \n")
        else:
            print ("입력이 누락되었습니다. 다시 입력해주세요")
            self.plus()
        return self.Book_lineup
       
    def search(self):
        print("1. 전체 입력으로 찾기 \n2. 개별 입력으로 찾기")
        search_number = int(input("어떻게 찾으시겠습니까? : "))
        if search_number == 1:
            search_book = input("도서명, 저자, 출판연도, 출판사명, 장르를 입력해주세요 : ").split()
            for i in range(len(self.Book_lineup)):
                if search_book == self.Book_lineup[i]:
                    print (self.Book_lineup[i])
                else:
                    print ("목록에 없습니다.")
        elif search_number == 2:
            search_menu = int(input("0.도서명, 1.저자, 2.출판연도, 3.출판사명, 4.장르 : "))
            userwant = input("찾으시는 것을 입력해주세요 : ")
            for k in range(len(self.Book_lineup)):
                if userwant == self.Book_lineup[k][search_menu]:
                    print (self.Book_lineup[k])      
        else:
            print ("잘못 입력하셨습니다.")
            self.search()

    def correct(self):
        self.all_books()
        choose_book = str(input("수정할 도서를 선택하세요 : "))
        for n in range(len(self.Book_lineup)):
            if choose_book == self.Book_lineup[n][0]:
                print ("0. 도서명, 1. 저자, 2. 출판연도, 3. 출판사명, 4. 장르") 
                fix = int(input("어떤 것을 수정하시겠습니까? : "))
                self.Book_lineup[n][fix] = input("수정할 내용을 입력해주세요 : ")
        return self.Book_lineup

    def delete(self):
        self.all_books()
        delete_book = str(input("삭제할 도서를 선택하세요 : "))
        for j in range(len(self.Book_lineup)):
            if delete_book == self.Book_lineup[j][0]:
                self.Book_lineup.pop(j)
                print('삭제되었습니다. \n')
    
    def all_books(self):
        for p in range(len(self.Book_lineup)):
            print (self.Book_lineup[p])

    def save(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'input.txt')
        Book_list = open(my_file,'w')
        for m in range(len(self.Book_lineup)):
            Book_list.writelines(' '.join(self.Book_lineup[m]))
            Book_list.writelines('\n')
        Book_list.close()