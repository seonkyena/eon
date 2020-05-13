n, m = list(map(int, input("작업 수 / 작업 번호  : ").split())) 
priority = list(map(int,input("작업 우선순위 : ").split()))  
 
number = list(range(len(priority)))
delay = 0

while True: 
    if priority[0] == max(priority):  
        delay += 1 
        if number[0] == m:
            print(delay,"분") 
            break 
        else:              
            number.pop(0) 
            priority.pop(0)
    else: 
        number.append(number.pop(0)) 
        priority.append(priority.pop(0))