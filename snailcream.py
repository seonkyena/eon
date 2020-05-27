number = int(input("숫자를 입력하세요 : "))
data = [[0] * number for i in range(number)] 

i = 0
j = -1 
n = 0 
s = 1

def DrG(i, j, n, s, number): 
    for p in range(1,number+1): 
        n = n + 1 
        j = j + s 
        data[i][j] = n 
    
    number = number - 1

    if number <= 0 : 
        return 0

    for p in range(1,number+1): 
        n = n + 1 
        i = i + s 
        data[i][j] = n 
         
    s = s * -1 
    return DrG(i, j, n, s, number)

DrG(i, j, n, s, number)
for i in range(number):
    print(data[i])