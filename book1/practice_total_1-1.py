#coding: UTF-8

list2 = list(range(2,11))

for i in list2:
    cnt = 0
    for j in list(range(1,i)):
        if i % j == 0:
            cnt += 1

    if cnt == 1:
        print (f"{i} is prime number")
    else:
        print (f"{i} is not prime number")
        
    
        
            
