import math
a = int(input())
cnt = 0
for i  in range(1,int(math.sqrt(a))):
    if a % i == 0: 
        print(i , end = " ")
