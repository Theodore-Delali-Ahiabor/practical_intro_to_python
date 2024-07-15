# This is based on the chapters in 'A Practical Introduction to Python Programming Heinold (PDF)
# Chapter 1 - Getting Started
  
class Section3:
    def afirstprogram():
        temp = eval(input('Enter a temperature in Celsius: '))
        print('In Fahrenheit, that is', 9/5*temp+32)
    
    def aSecondProgram():
        num1 = eval(input('Enter the first number: '))
        num2 = eval(input('Enter the second number: '))
        print('The average of the numbers you entered is', (num1+num2)/2)

    def sectionTestProgram():
        print('Welcome to my pyton lessons')


class Section5:
    def gettingTextInput():
        name = input('Enter your name: ')
        print('Hello, ', name)

    def gettingNumericInput():
        num = eval(input('Enter a number: '))
        print('Your number squared:', num*num)
    
    def sectionTestProgram():
        name =input('Enter your full name: ')
        age = eval(input('Enter your current age: '))
        print('Hello', str(name), ', you are', str(age), 'years old')


class Section7:
    def optionalArguments1():
        print ('The value of 3+4 is', 3+4, '.')
        print ('The value of 3+4 is ', 3+4, '.', sep='')
    
    def optionalArguments2():
        print('On the first line', end='')
        print('On the second line')

    def aSecondExample():
        temp = eval(input('Enter a temperature in Celsius: '))
        f_temp = 9/5*temp+32
        print('In Fahrenheit, that is', f_temp)
        if f_temp > 212:
            print('That temperature is above the boiling point.')
        if f_temp < 32:
            print('That temperature is below the freezing point.')

    def sectionTestProgram():
        print ('The value of 3+4 is', 'welcome', 3+4, '.', sep='$')


class Section8:
    def exercise1():
        print('*'*12)
        print('*'*12)
        print('*'*12)
        print('*'*12)

    def exercise2():
        print('*'*12)
        print('*', ' '*8, '*')
        print('*', ' '*8, '*')
        print('*'*12)
    
    def exercise3():
        print('*')
        print('*'*2)
        print('*'*3)
        print('*'*4)
    
    def exercise4():
        print((512 - 282) / (47.48 + 5))
    
    def exercise5():
        num = eval(input('Enter a number: '))
        print('The square of ', num, ' is ', num*num, '.', sep='')

    def exercise6():
        num = eval(input('Enter a number: '))
        print(num, 2*num, 3*num, 4*num, 5*num, sep='---')

    def exercise7():
        num = eval(input('Enter a weight in kilograms: '))
        print(num, 'kg is equal to ', num*2.2, 'pounds')

    def exercise8():
        num1 = eval(input('Enter the first number: '))
        num2 = eval(input('Enter the second number: '))
        num3 = eval(input('Enter the third number: '))
        total = num1+num2+num3
        average = total/3
        print('The total of', num1, num2, num3, 'is:', total)
        print('The average of', num1, num2, num3, 'is:', average)

    def exercise9():
        cost = eval(input('Enter the cost of the meal: '))
        tip_per = eval(input("Enter the percentage tip you want to leave without the '%' symbol: "))
        tip = (tip_per/100)*cost
        print('Your tip is: ', tip)
        print('The total cost is: ', cost+tip)
