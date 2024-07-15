#This is based on the chapters in 'A Practical Introduction to Python Programming Heinold (PDF)
#Chapter 2 - For Loops

class section1:
    def sectionTestProgram():
        for i in range(5):
            print('*'*i)


class section5:
    def exercise1():
        for i in range(100):
            print('Theodore')

    def exercise2():
        for i in range(100):
            print('Rhody'*100,end='')

    def exercise3():
        for i in range(100):
            print(i,'-- Theodore')

    def exercise4():
        for i in range(20):
            print(i,'--',i*i)
    
    def exercise5():
        for i in range(8,90,3):
            print(i,end=', ')

    def exercise6():
        for i in range(100,1,-2):
            print(i,end=', ')
    
    def exercise7():
        for i in range(10):
            print('A',end='')
        for i in range(7):
            print('B',end='')
        for i in range(8):
            print('C',end='')
            print('D',end='')
        print('E',end='')
        for i in range(6):
            print('F',end='')
        print('G',end='')

    def exercise8():
        name = input('Enter your name: ')
        num = eval(input('Enter how many times to print your name: '))
        for i in range(num):
            print(name)

    def exercise9():
        num = eval(input('Enter how many Fibonacci numbers to print: '))
        #Decalaire two numbers num1 and num2
        num1 = 0
        num2 = 1
        #Intanciate a variable sum, which is the sum of num1 and num2
        sum = num1 + num2
        #Print the sum
        print(sum, end=', ')
        #Start a for loop with range, the number provided by the user.
        for i in range(1,num):
            #Assign the value of num2 to num1
            num1 = num2
            #Assign the value of sum to num2
            num2 = sum
            #Print the sum
            print(sum,end=', ')
            #Assign the sum of num1 and num2 to the variable sum
            sum = num1 + num2
            
    def exercise10():
        for i in range(4):
            print('*'*10)

    def exercise11():
        print('*'*10)
        for i in range(2):
            print('*',' '*8,'*',sep='')
        print('*'*10)

    def exercise12():
        for i in range(1,4):
            print('*'*i)

    def exercise13():
        for i in range(4,0,-1):
            print('*'*i)

    def exercise14():
        num = eval(input('Enter the height of your diamond, ODD Numbers only: '))
        
        median = num/2 +1
        step = 1
        for i in range(1,num,2):
            print(' '* int(median-step),'*' * i, sep = '')
            step +=1
        
        step = -1
        for i in range(num,0,-2):
            print(' '* int(step+1),'*' * i, sep = '')
            step +=1
            
    def exercise15():
        num = eval(input('Enter how large your letter A should be, Value must be greater than 5: '))

        median = num/2 +1
        step = 0
        print(' '* int(median-step+1),'*', sep = '')
        for i in range(1,num,2):
            print(' '* int(median-step),'*',' ' * i,'*', sep = '')
            step +=1
            if (step==1):
                print(' '* int(median-step),'*','*' * int(i*step+2),'*', sep = '')
                step +=1
                break
        for j in range(1,num-1,2):
            print(' '* int(median-step),'*',' ' * int(j+4),'*', sep = '')
            step +=1