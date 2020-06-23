import sys
import t2

class trainUser:
    def __init__(self):
        self.userinputdata = []

    def userReservationInfo(self, userinputdata):
        buffer = input('찾으시는 기차 정보를 입력해주세요 - ex) 09:34(시간) 서울(출발역) 부산(도착역) KTX(열차종류) : ')
        self.userinputdata = buffer.split()#['0705', '서울', '부산', 'KTX']

        return self.userinputdata

    def cancel_reserv(self):
        self.t2.reserv_train()
        print ("1. 예매 내역을 출력합니다. ")
        print ("2. 예매 내역을 취소합니다. ")
        print ("3. 뒤로가기 ")
        
        cancel_input = int(input("메뉴를 선택해주세요 : "))
        if cancel_input == 1:
            print (self.complete)
            if not self.complete:
                print ("예매된 내역이 없습니다.")
            return self.complete   
        elif cancel_input == 2:
            if self.complete:
                print ("왼쪽부터 0번 ~ ",len(self.complete)-1,"번 입니다.")
                print (self.complete)
                cancel_number = int(input("몇 번을 취소하시겠습니까 ? : "))
                for g in range(len(self.trainlines)):
                    if self.complete[cancel_number] == self.trainlines[g]:
                        self.trainlines[g][-1] += 1  
                        print ("예약이 취소되었습니다.")
                        self.complete.pop(cancel_number)
            elif not self.complete:
                print ("예매 된 내역이 없습니다.")
                self.train_menu()
        elif cancel_input == 3:
            self.train_menu()
        else:
            print ("번호가 없습니다. 다시 입력해주세요 : ")
            self.cancel_reserv()
        return self.trainlines, self.complete







