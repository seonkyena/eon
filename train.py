import sys

class reservation():
    def __init__(self):
        self.train_lines = []
        self.depart_time = []

    def __list__(self):
        try:
            self.apahwkd = open("C:/Users/IBK/Documents/kyx/eon/TrainList.txt", 'r')
            self.train_lines = self.apahwkd.readlines()
            self.train_lines.pop(0)
            self.train_lines.close()
            return self.train_lines
        except IOError as e:
            print("{0}".format(e))

    def select_menu(self):
        while True:
            print("1. 빠른 시간 기차 검색 및 예매 /n 2. 전체 기차 리스트 출력 /n 3. 나의 예매 현황 출력 및 예매 취소 /n 4.프로그램 종료")
            try:
                menu = int(input("메뉴를 선택하세요. : "))
            except ValueError:
                print("입력 오류입니다.")

            if menu == 1:
                self.train_search()
            elif menu == 2:
                self.train_print()
            elif menu == 3:
                self.train_mine()
            elif menu == 4:
                print("예매를 종료합니다.")
                break
            else:
                print("입력 오류입니다.")   
                self.select_menu()

    def train_time(self):