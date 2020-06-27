import sys
import copy

lineup = open("C:/Users/IBK/Documents/kyx/eon/TrainList.txt", 'r')
train_lines = []
while True:
    try:
        line = lineup.readline().split()
        train_lines.append(line)
        if not line:
            break
    except IOError:
        print('파일이 존재하지 않습니다')
lineup.close()
train_lines.pop(0)
train_lines.pop(-1)

modyList = copy.deepcopy(train_lines)
completelist = []
add_ress = None

for i in range(len(modyList)):
    modyList[i].pop(2)
    modyList[i][0] = modyList[i][0].replace(":", "")
    modyList[i][0] = int(modyList[i][0])

class TGVisFrench:

    def menulist(self):
        while True:
            print("1. 빠른 시간 기차 검색 및 예매하기 \n2. 전체 기차 편성 보기 \n3. 예매 현황 보기, 예매 취소하기 \n4. 프로그램 종료")
            try:
                menu = int(input("메뉴를 입력하세요 : "))
            except ValueError:
                print("올바르지 않은 입력입니다. 다시 선택해주세요")
                self.menulist()

            if menu == 1:
                self.search_train()
            elif menu == 2:
                self.all_lines()
            elif menu == 3:
                self.reserv_lines()
            elif menu == 4:
                self.program_off()
                break
            else:
                print("메뉴에 없습니다. 다시 선택해주세요")
                self.menulist()

    def search_train(self):
        userspick = list(input("출발시간, 출발역, 도착역, 열차종류 입력 예) 07:20 서울 부산 KTX 입력 : ").split())
        tmp_mytime = userspick[0].replace(":", "")
        mytime = int(tmp_mytime[:2]) * 60 + int(tmp_mytime[2:4])
        userspick[0] = close_time(mytime)

        withoutseat = copy.deepcopy(modyList)
        for n in range(len(modyList)):
            withoutseat[n].pop()        #입력과 같은 리스트를 만들기 위해 좌석수를 삭제

        final_list = []
        for k in range(len(withoutseat)):
            if withoutseat[k] == userspick:
                final_list = withoutseat[k].copy()
                final_list.append(train_lines[k][5])
                add_ress = k     #선택된 기차편의 주소

        a, b = divmod(final_list[0], 100)
        hour = str(a)
        minute = str(b)
        final_list[0] = ''.join(['0', hour, ':', minute])
        print('가장 가까운 기차입니다.')
        print(final_list)

        reservation = input("\n해당 기차표를 예매하시겠습니까? (Y/N) 입력 : ")
        if (reservation == 'Y') or (reservation == 'y'):
            if train_lines[add_ress][5] != 0:
                completelist.append(train_lines[add_ress])
                train_lines[add_ress][5] = int(train_lines[add_ress][5]) - 1
                print("\n예매가 완료되었습니다.")
            else:
                print("\n매진입니다.")
                self.menulist()
        elif (reservation == 'N') or (reservation == 'n'):
            self.menulist()
        else:
            print("올바르지 않은 입력입니다. 한영키를 확인해주세요. \n")
            self.menulist()
        return add_ress, completelist

    def all_lines(self):
        print("1. 전체 편성 보기 \n2. 뒤로가기")
        all_lines_menu = input("입력 : ")
        if all_lines_menu == "1":
            for p in range(len(train_lines)):
                if train_lines[p][5] == 0:
                    train_lines[p][5] = "매진"
                print(train_lines[p])
            print("\n")
        elif all_lines_menu == "2":
            self.menulist()
        else:
            print('다시 입력해주세요')
            self.all_lines()

    def reserv_lines(self):
        print("1. 예매내역을 출력합니다. \n2. 예매내역을 취소합니다. \n3. 이전 메뉴로 돌아갑니다.")
        select = input("메뉴를 선택하세요. : ")
        if select == "1":
            print("예매 내역입니다.")
            print(completelist)
            print("\n")
        elif select == "2": 
            cancel = input("\n예매를 취소하시겠습니까? (Y/N) 입력 : ")
            if (cancel == 'Y') or (cancel == 'y'):
                print ("예약번호 0번부터 시작합니다.")
                print (completelist)
                cancel_number = int(input("몇 번을 취소하시겠습니까 ? : "))
                for g in range(len(train_lines)):
                    if not completelist:
                        print ("예매 된 내역이 없습니다.")
                        self.menulist()
                    else:
                        if completelist[cancel_number] == train_lines[g]:
                            train_lines[g][5] = train_lines[g][5] + 1
                            completelist.pop(cancel_number)
                            print ("\n예약이 취소되었습니다. \n메뉴로 돌아갑니다. \n")
                            break
            elif (cancel == 'N') or (cancel == 'n'):
                print('뒤로 갑니다.')
                self.reserv_lines()
        elif select == "3":
            self.menulist()
        else:
            self.reserv_lines()       

    def program_off(self):
        sys.exit()

def close_time(mytime):
    onlylist = [365, 395, 435, 522]
    real_time_list = [605, 635, 715, 842]
    abs_list = []
    for i in range(len(onlylist)):
        abs_list.append(abs(mytime - onlylist[i]))
    add_ress = abs_list.index(min(abs_list))
    return real_time_list[add_ress]

if __name__ == "__main__":
    kyx = TGVisFrench()
    print(kyx.menulist())