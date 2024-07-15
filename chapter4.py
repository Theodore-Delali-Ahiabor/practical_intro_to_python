#This is based on the chapters in 'A Practical Introduction to Python Programming Heinold (PDF)
#Chapter 4 - If Statements


from random import randint


class section1:
    def example1():
        from random import randint
        num = randint(1,10)
        guess = eval(input('Enter your guess: '))
        if guess==num:
            print('You got it!')
        else:
            print("Sorry th enumber is: ",num)


class section5:
    def exercise1():
        num = eval(input("Enter a length in centimeters: "))
        if num < 0 :
            print("Invalid Input")
        else:
            print(num,"centimeters equals",num*2.54,"inches")

    def exercise2():
        temp = eval(input("Enter a temperature: "))
        unit = input("What unit is the temperature in?, Enter 'F' or 'f' For Fahrenheit or 'c' or 'C' for Celsius ")

        if(unit =='c' or unit == 'C'):
            print(temp,"C equals",((9/5) * temp) + 32,"F")
        elif(unit == 'f' or unit == 'F'):
            print(temp,"F equals", 5/9 * (temp - 32),"C")
        else:
            print("Invalid unit enterd")

    def exercise3():
        temp = eval(input("Enter a temperature in celsius: "))
        if temp < -273.15:
            print("The temperature is invalid because it is below absolute zero")
        elif temp == -273.15:
            print("The temperature is absolute 0")
        elif(-273.15 <= temp <= 0):
            print("The temperature is below freezing")
        elif(temp == -273.15):
            print("The temperature is at the freezing point")
        elif(0 <= temp <= 100):
            print("The temperature is in the normal range")
        elif(temp == 100):
            print("The temperature is at the boiling point")
        elif(temp>100):
            print("The temperature is above the boiling point")

    def exercise4():
        credit = eval(input("How many creduts have you taken? "))
        if credit <= 23 :
            print("You are a freshman")
        elif 24 <= credit <= 53 :
            print("You are a sophomore")
        elif 53 <= credit <= 83 :
            print("You are a junior")
        elif credit >= 84 :
            print("You are a senior")
    
    def exercise5():
        from random import randint
        num = randint(1,11)
        guess = eval(input("Enter a number in the range 1 - 10 :"))
        if num == guess :
            print("huraay!!! you got it right")
        else:
            print("ooooo!!! your guess is wrong. The number is",num)

    def exercise6():
        items = eval(input("How many items do you want to buy? "))
        if items < 10 :
            print("Total cost is GHS",items*12)
        if 10 <= items <= 99 :
            print("Total cost is GHS",items*10)
        if items >= 100 :
            print("Total cost is GHS",items*7)

    def exercise7():
        #Solution is incomplete
        num1 = eval(input("Enter the first number: "))
        num2 = eval(input("Enter the second number: "))
        print(round(round(num1 - int(num1),3)*1000))
        if((num1 % 1000 <= round(num1,3) <= round(num2,3)) or (round(num1,3) <= round(num2,3))):
            print("Close")
        else:
            print("Not close")
     
    def exercise8():
        year = eval(input("Enter a year: "))
        if year % 4 == 0 or (year%100 == 0 and year % 400 == 0):
            print(year,"is a leap year.")
        else:
            print(year,"not a leap year.")
        
    def exercise9():
        num = eval(input("Enter a number: "))
        for i in range (1,num):
            if(num % i == 0):
                print(i)

    def exercise10():
        from random import randint
        for i in range(1,11):
            num1 = randint(1,10)
            num2 = randint(1,10)
            print("Question ", i, " : ",num1, " x ", num2, " = ",end=" ")
            ans = eval(input())
            if num1 * num2 == ans :
                print("Right!!")
            else:
                print("Wrong. The answer is", num1*num2)
    
    def exercise11():
        hour = eval(input("Enter hour: "))
        m = eval(input("am (1) or pm (2)?"))
        ahead = eval(input("How many hours ahead?"))
        new_hour = hour + ahead
       
        if (m == 1):
            if(((new_hour)//12)%2 == 0 ):
                print("The new hour is ", new_hour % 12, "am")
            else:
                print("The new hour is ", new_hour % 12, "pm")
        elif(m == 2):
            if(((new_hour)//12)%2 == 0 ):
                print("The new hour is ", new_hour % 12, "pm")
            else:
                print("The new hour is ", new_hour % 12, "am")
    
    def exercise12():
        for i in range(200):
            if ((i % 5 == 2) and (i % 6 == 3) and (i % 7 == 2)):
                print("There are",i,"number of cadys in the jar")
    
    def exercise13():
        from random import randint       
        score = 0 
        for i in range(1,6):
            print("Round",i)
            guess = eval(input("Enter (1) for Rock (2) for Paper (3) for Scissors: "))
            num = randint(1,3)
            if guess == num :
                score += 1
                print("Excellent!!!")
            else:
                if num == 1 :
                    print("Faild. computer played 'Rock' ") 
                elif num == 2 :
                    print("Faild. computer played 'Paper' ")
                else:
                    print("Faild. computer played 'Scissors' ")
        
        if(score > 3):
            print("You won!!")
        else:
            print("Computer won")