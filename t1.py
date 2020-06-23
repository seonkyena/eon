import sys
import copy
import t3

class trainserver:
    def __init__(self):
        self.trainlines = []
        self.t3_help = t3.trainUser()

    def T_list(self):
        try:
            self.Train_List = open("C:/Users/IBK/Documents/kyx/eon/TrainList.txt", 'r')
            self.trainlines = self.Train_List.read().splitlines()
            self.trainlines.pop(0)
            self.Train_List.close()
            return self.trainlines
        except IOError:
            print ("IOError가 일어났습니다. 파일이 없어용")
    
    def calculate(self, closeTime, userinputdata):
        self.t3_help.userinputdata()
        self.closeTime = []
        normaltime = []
        copylines = copy.deepcopy(self.trainlines)
        for i in range(len(copylines)):
            if copylines[i][1] != self.userinputdata[1]:
                copylines[i][0] = '00:00'
            if copylines[i][3] == self.userinputdata[2]:
                copylines[i][0] = '00:00'
            if copylines[i][4] == self.userinputdata[3]:
                copylines[i][0] = '00:00'

        userinputtime = int(self.userinputdata[0][:2]) * 60 + int(self.userinputdata[0][3:])
        for i in range(len(copylines)):
            traintime = int(copylines[i][0][:2]) * 60 + int(copylines[i][0][3:])
            normaltime.append(abs(userinputtime -traintime))

        self.closeTime = normaltime.index(min(normaltime))
        return self.closeTime

    def all_lines(self):
        for i in range(len(self.trainlines)):
            if self.trainlines[i][5] == '0':
                self.trainlines[i][5] = '매진'
            print(i, '. ', ' '.join(self.trainlines[i]))