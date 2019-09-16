def fizzBuzz(num):
    if num%3 == 0 and num%5 == 0:
        return "fizzBuzz"
    elif num %3 == 0:
        return "fizz"
    elif num%5 == 0:
        return "buzz"
    else:
        return num


for num in range(1,100):
    print (fizzBuzz(num))
    print (type(fizzBuzz(num))) 

    
