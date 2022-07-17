def square(num,k):#Method 1: 2 for loop
    if num <= 0:
        raise TypeError(f"Sorry,for {num} no numbers below zero")
    if not type(k) is str:
        raise TypeError(f"for {k} Only strings are allowed")
    else:
        for i in range(num):
            if i == 0 or i == num - 1:
                print(k*num)
            else:
                print(k,end="")
                for i in range(num-2):
                    print(" ",end="")
                print(k)
square(6,"*")
#############################
def squr(num,k):# method 2: 3 for loop but with space in first and last line
    if num<=0:
        raise TypeError(f"Sorry,for {num} no numbers below zero")
    if not type(k) is str:
        raise TypeError(f"for {k} Only strings are allowed")
    else:
        for i in range(num):
            if i == 0:
                for j in range(num):
                    print(k,end=" ")
                print()
            if i == num-1:
                for j in range(num):
                    print(k,end=" ")
            else:#i!=0 and i!=num-1:
                print(k, end=" ")
                for i in range(num - 2):
                    print(" ", end=" ")
                print(k)
squr(6,"*")