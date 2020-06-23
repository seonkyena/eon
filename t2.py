import sys
import t1
import t3

class trainsystem:
    def __init__(self):
        self.userselect = None
        self.complete = []
        self.t1_help = t1.trainserver()
        self.t3_help = t3.trainUser()

    def train_menu(self):
        while True:
            print("1. 빠른 시간 기차 검색 및 예매하기 /n 2. 전체 기차 시간대 보기 /n 3. 예매 현황 보기, 예매 취소하기 /n 4. 프로그램 종료")
            try:
                menu = int(input("메뉴를 선택 해주세요 : "))
            except ValueError:   #int형이 아닌 문자형이나 형 오류를 받았을때 실행
                print("올바르지 않은 입력입니다.")    
                self.train_menu() 
            
            if menu == 1:
                self.reserv_train()
            elif menu == 2:
                self.t1_help.all_lines()
            elif menu == 3:
                self.t3_help.cancel_reserv()
            elif menu == 4:
                print(" 프로그램 종료하겠습니다.")
                self.program_off()
                break
            else:
                print ("메뉴에 없습니다. 다시 번호를 입력해주세요.")
                self.train_menu()

    def reserv_train(self):
        self.t1_help.calculate()
        print("입력하신 시간에 가장 가까운 기차입니다.")
        print(self.closetime)
        print()
        answer = input("예매하시겠습니까? Y / N")
        if (answer == 'Y') or (answer == 'y'):
            for k in range(len(self.trainlines)):
                if self.trainlines[k] == self.closetime:
                    if (self.closetime[-1] == 0) or (self.closetime[-1] == '매진'):
                        print ("매진 되었습니다.")
                    else: 
                        self.closetime[-1] = self.closetime[-1] - 1
                        self.trainlines[k][-1] = self.closetime[-1]
                        self.complete.append(self.trainlines[k])
                        print ("예매 되었습니다.")
        else:
            self.train_menu()

    def program_off(self):
        sys.exit()

if __name__ == "__main__":
    kyx = trainsystem()
    print(kyx.train_menu)