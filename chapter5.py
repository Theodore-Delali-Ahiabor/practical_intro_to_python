#This is based on the chapters in 'A Practical Introduction to Python Programming Heinold (PDF)
#Chapter 5 - Miscellaneous Topics I


class section1:
    def example1():
        count = 0
        for i in range(10):
            num = eval(input('Enter a number: '))
            if num>10:
                count=count+1
        print('There are', count, 'numbers greater than 10.')

    def example2():
        count1 = 0
        count2 = 0
        for i in range(10):
            num = eval(input('Enter a number: '))
            if num>10:
                count1=count1+1
            if num==0:
                count2=count2+1
        print('There are', count1, 'numbers greater than 10.')
        print('There are', count2, 'zeroes.')
    
    def example3():
        count = 0
        for i in range(1,101):
            if (i**2)%10==4:
                count = count + 1
        print(count)

class section2:
    def example1():
        s = 0
        for i in range(1,101):
            s = s + i
        print('The sum is', s)
    
    def example2():
        s = 0
        for i in range(10):
            num = eval(input('Enter a number: '))
            s = s + num
        print('The average is', s/10)


class section9:
    def exercise1():
        count = 0
        for i in range(1,101):
            if ((i ** 2) % 10 == 1):
                count +=1
        print("the squares of the numbers from 1 to 100 end in a 1 =",count)

    def exercise2():
        count1 = 0
        count2 = 0
        for i in range(1,101):
            if ((i ** 2) % 10 == 4):
                count1 +=1
            if ((i ** 2) % 10 == 9):
                count2 +=1
        print("the squares of the numbers from 1 to 100 end in a 4 =",count1)
        print("the squares of the numbers from 1 to 100 end in a 9 =",count2)

    def exercise3():
        from math import log
        num = eval(input("Enter a number: "))
        sum = 0 
        for i in range(1,num+1):
            sum += 1/i
        
        print("Ans =",sum - log(num))

    def exercise4():
        sum  = 0
        for i in range(1, 2001):
            sum += i - (i +1)
        print(sum)

    def exercise5():
        num = eval(input("Enter a number: "))
        sum  = 0
        for i in range(1, num+1):
            if num % i == 0 :
                sum += i 
        print("Sum of devisors =", sum)

    def exercise6():
        """num = eval(input("Enter a number: "))
        sum  = 0
        for i in range(1, num):
            if num % i == 0 :
                sum += i 
        if(sum == num):   
            print("Is a perfect number", sum)
        else:
            print("Not a perfect number ")"""

        for i in range(1, 10000):
            sum  = 0
            for j in range(1,i):
                if i % j == 0 :
                    sum += j 
            if(sum == i):   
                print(i,"is a perfect number")
             

    def exercise7():
        from math import sqrt
        found = False
        num = eval(input("Enter a number: "))
        for i in range(1,num):
            if num % i == 0:
                if sqrt(i) == int(sqrt(i)) != 1:
                    found = True   
        if found == False:
            print(num,"is a square free number")
        else:
            print(num,"is NOT a square free number")

    def exercise8():
        x = 2
        y = 3 
        z = 5
        
        temp_x = x
        temp_y = y
        temp_z = z
        x = temp_y
        y = temp_z
        z = temp_x
        print("X =",x)
        print("Y =",y)
        print("Z =",z)

    def exercise9():
        from math import sqrt
        for i in range(1,1001):
            if not (sqrt(i) == int(sqrt(i))):
                print(i)

    def exercise10():
        heighest = 0
        second_heighest = 0
        lowest = 100
        second_lowest = 100
        sum = 0
        above = 0
        for i in range(1,11):
            num = eval(input("Enter score "+str(i)+" ",))
            sum += num
            if num < second_lowest:
                second_lowest = lowest
                lowest = num
                
                
            if num > heighest:
                second_heighest = heighest
                heighest = num
                
            if num > 100:
                above += 1
            
        print("(a) The Heighest =", heighest,"Lowest =", lowest)
        print("(b) The average =", sum/10)
        print("(c) The second Heighest =", second_heighest)
        print("(d) Numbers greater than 100 =", above)
        print("(e) Average without the two lowest =", (sum-(lowest + second_lowest))/8)
        print("second lowest",second_lowest)

    def exercise11():
        num = eval(input("Enter a number: "))
        fac = 1
        for i in range(1, num + 1):
            fac *= i
        print(fac)
            
    def exercise12():
        from random import randint
        score = 0 
        for i in range(1,6):
            print("ROUND",i)
            guess = eval(input("Enter a number btween 1 and 10: "))
            num = randint(1,10)
            if num == guess :
                print("Right")
                score += 10
            else:
                print("Wrong, the number is",num)
                score -= 1
        print("Score =",score)

    def exercise13():
        from random import randint
        score  = 0 
        for i in range(1,11):
            num1 = randint(1,10)
            num2 = randint(1,10)
            print("Question ", i, " : ",num1, " x ", num2, " = ",end=" ")
            ans = eval(input())
            if num1 * num2 == ans :
                print("Right!!")
                score += 1
            else:
                print("Wrong. The answer is", num1*num2)
        if score > 8 :
            print("Excellent")
        elif score > 5 :
            print("Good job")
        elif score > 3 :
            print("More room for improvement")
        else:
            print("Failed try again")

    def exercise14():
        from random import randint
        
        keep_count = 0
        change_count = 0
        for i in range(1,10001):
            prize = randint(1,5)
            guess = randint(1,5)
            choice = randint(1,3)
            
            if choice == 1 :
                #choice to keep selection
                if prize == guess :
                    keep_count += 1
            else:
                #choice to change selection
                guess =randint(1,4)
                if prize == guess :
                    change_count += 1
        print(keep_count)
        print("Keep win chance =", (keep_count/10000)*100,"%")
        print("Change win chance =", (change_count/10000)*100,"%")
