#coding: UTF-8

num = int(input("please input number: "))
list2 = list(range(2,num+1))

for i in list2:
    cnt = 0
    for j in list(range(1,i)):
        if i % j == 0:
            cnt += 1

    if cnt == 1:
        print (f"{i} is prime number")
    else:
        print (f"{i} is not prime number")
        
    
        
            
