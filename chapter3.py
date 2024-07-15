#This is based on the chapters in 'A Practical Introduction to Python Programming Heinold (PDF)
#Chapter 3 - Numbers


class section4:
    def randintExample():
        from random import randint
        x = randint(1,10)
        print('A random number between 1 and 10: ', x)


class section5:
    def mathFunctions():
        from math import sin, pi
        print('Pi is roughly', pi)
        print('sin(0) = ', sin(0))

    def builtInMathFunctions():
        print("The absolute value of -20 = ",end='')
        print ( abs(-20))
        print("The round of 2.5165 to two decimal places = ",end='')
        print( round(2.5165,2))


class section6:
    def gettingHelp():
        import math 
        print(help(math))

    
class section8:
    from random import randint
    def exercise1():
        from random import randint
        for i in range(50):
            print(randint(3,6))

    def exercise2():
        from random import randint
        x = randint(1,50)
        y = randint(2,5)
        print(x**y)

    def exercise3():
        from random import randint
        x = randint(1,10)
        for i in range(x):
            print("Theodore")

    def exercise4():
        from  random import uniform
        x = uniform(1.00,10.00)
        print(round(x,2))

    def exercise5():
        from random import randint
        for i in range(1,50):
            print(randint(1,i+1))

    def exercise6():
        x = eval(input("Enter the X value: "))
        y = eval(input("Enter the Y value: "))
        print((abs(x-y))/(x+y))

    def exercise7():
        x = eval(input("Enter a value between -180 and 180: "))
        print((x+180)%360)
        
    def exercise8():
        x = eval(input("Enter the time value in seconds: "))
        print("The time reads",x//60,":",x%60)

    def exercise9():
        hour = eval(input("Enter hour between 1 and 12: "))
        ahead = eval(input("How many hours ahead? : "))
        print("New hour:", (hour+ahead)%12,"O'Clock")

    def exercise10a():
        num = eval(input("Enter a power: "))
        print("The last digit of",2**num,"is",(2**num)%10)

    def exercise10b():
        num = eval(input("Enter a power: "))
        print("The last two digits of",2**num,"is",(2**num)%100)

    def exercise10c():
        num = eval(input("Enter a power: "))
        times = eval(input("How many digits from the back do you want to display: "))
        print("The last",times,"digit(s) of",2**num,"is",(2**num)%(10**times))

    def exercise11():
        num = eval(input("Enter a weight in kilograms: "))
        print("The weight converts to",round(num*2.20462,10),"pounds")

    def exercise12():
        from math import factorial
        num = eval(input("Enter a number: "))
        print("The factorial of",num,":",factorial(num))
        
    def exercise13():
        from math import sin, cos, tan
        num = eval(input("Enter a number: "))
        print("The Cosine of",num,":",cos(num))
        print("The Sine of",num,":",sin(num))
        print("The Tangent of",num,":",tan(num))

    def exercise14():
        from math import sin
        num = eval(input("Enter an angle in degrees: "))
        print("The Sine of",num,"degrees:",sin(num))

    def exercise15():
        from math import sin,cos
        for i in range(0,346,15):
            print(i,"--- Sine:",round(sin(i),4),"Cosine:",round(cos(i),4))

    def exercise17():
        year = eval(input("Enter a year: "))
        count = 0
        for i in range(1600,year):
            if(i % 4 == 0 or (i % 400 == 0 and i % 100 ==0)):
                #print(i)
                count+=1
        print("There are",count,"leep years between 1600 and",year)

    def exercise19():
        width = eval(input("Enter the width of the rectangle: "))
        height = eval(input("Enter the height fo the rectangle: "))
        for i in range(0,(height*width),1):
            print(i%(width+1), end=" ")
            if((i+1) % width == 0):
                print(" ")
           
       
                
            