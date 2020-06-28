import sys
import os
import BuchDB

class BookSS:
    def __init__(self):
        self.Data0fBook = BuchDB.BuchData()
        self.Data0fBook.buch_list()

    def menulist(self):
        while True:
            print("1. 도서 추가 \n2. 도서 검색 \n3. 도서 정보 수정 \n4. 도서 삭제 \n5. 도서 목록 출력 \n6. 저장 \n7. 프로그램 나가기 ")
            try:
                select = int(input("메뉴를 선택해주세요 : "))
            except ValueError:
                print("올바르지 않은 입력입니다. 다시 선택해주세요. \n")
                continue
            
            if select == 1:
                self.Data0fBook.plus()
            elif select == 2:
                self.Data0fBook.search()
            elif select == 3:
                self.Data0fBook.correct()
            elif select == 4:
                self.Data0fBook.delete()
            elif select == 5:
                self.Data0fBook.all_books()
            elif select == 6:
                self.Data0fBook.save()
            elif select == 7:
                print("프로그램을 종료합니다.")
                self.Data0fBook.save()
                break
            else:
                print ("메뉴에 없습니다. 다시 선택 해주세요.")
                self.menulist()
    
if __name__ == "__main__":                    
    kyx = BookSS()
    print (kyx.menulist())