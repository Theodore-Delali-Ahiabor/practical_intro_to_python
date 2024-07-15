#This is based on the chapters in 'A Practical Introduction to Python Programming Heinold (PDF)
#Chapter 7 - Lists



class section6:
    def example1():
        from random import randint
        L = []
        for i in range(50):
            L.append(randint(1,100))
        print(L)

    def example2():
        L = [1,2,3,4,5]
        for i in range(len(L)):
            L[i] = L[i]**2
        print(L)
    
    def example3():
        from random import randint
        L = []
        for i in range(50):
            L.append(randint(1,100))
        count = 0
        for item in L:
            if item>50:
                count=count+1
        print(count)

    def example4():
        from random import randint
        L = []
        for i in range(50):
            L.append(randint(1,100))

        frequencies = []
        for i in range(1,101):
            frequencies.append(L.count(i))
        print(frequencies)

    def example5():
        from random import randint
        L = []
        for i in range(50):
            L.append(randint(1,100))
        scores = L[:]
        scores.sort()
        print('Two smallest: ', scores[0], scores[1])
        print('Two largest: ', scores[-1], scores[-2])
    

class section7:
    def exercise1():
        L = eval(input("Enter a list of integers separating the items with commas: "))
        print(L)
        print("(a) The total number of items in the list =",len(L))
        print("(b) The last item in the list =",L[-1])
        print("(c) The list in reserve order =",L[::-1])
        if 5 in L:
            print("(d) = Yes")
        else:
            print("(d) = No")
        print("(e) The number of 5's in the list =",L.count(5))
        new_l = []
        for s in range(len(L)):
            new_l.append(L[s])
        del new_l[0]
        del new_l[-1]
        new_l.sort()
        print("(f) =", new_l)
        count = 0
        for i in L:
            if i < 5 :
                count +=1
        print("(g) The number of items less than 5 =", count)
        
    def exercise2():
        from random import randint
        L = []
        for i in range(20):
            L.append(randint(1,101))
        print("(a) The list is =",L)
        print("(b) The average of the List =", sum(L)/len(L))
        print("(c) The largest value in the List =", max(L))
        print("(c) The smallest value in the List =", min(L))
        new_l = []
        for c in range(len(L)):
            new_l.append(L[c])
        new_l.sort()
        print("(d) The second largest value in the List =", new_l[-2])
        print("(d) The second smallest value in the List =", new_l[1])
        count = 0
        for i in L:
            if i % 2 == 0 :
                count +=1
        print("(e) The number of even numbers in the List =", count)
    
    def exercise3():
        L = [8,9,10]
        L.insert(1,17)
        add = [4,5,6]
        L = L + add
        del L[0]
        L.sort()
        L = L*2
        L.insert(3,25)
        print("The new list is =", L)
    
    def exercise4():
        l = eval(input("Enter a list of integers between 1 and 12 separating the items with commas: "))
        L = []
        for c in l:
            L.append(c)
        for i in range(len(L)):
            if L[i] > 10:
                L[i] = 10
                #L.insert
        print(L)

    def exercise5():
        l = eval(input("Enter a list of strings putting each string in double or single qoutes and separating the items with commas: "))
        L = []
        for c in l:
            L.append(c[1:])
        print(L)

    def exercise6():
        L1 = [] 
        L2 = []
        L3 = []
        for i in range(50):
            L1.append(i)
        for i in range(1,51):
            L2.append(i**2)
        l = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(l)):
            L3.append(l[i]*(i+1))
        print("(a) =",L1)
        print("(b) =",L2)
        print("(c) =",L3)

    def exercise7():
        print("Enter lists o the same lenght (same number of items) : ")
        L1 = eval(input("Enter list 1 of integers separating the items with commas: "))
        L2 = eval(input("Enter list 2 of integers separating the items with commas: "))
        L3 = []
        if len(L1) == len(L2):
            for i in range (len(L1)):
                L3.append(L1[i] + L2[i])
        else:
            print("List 1 and 2 have different number of items")
        print("The sum =",L3)

    def exercise8():
        num = eval(input("Enter an integer: "))
        L = []
        for i in range(1,num+1):
            L.append(i)
        print(L)

    def exercise9():
        from random import randint
        l = [2,3,4,5,6,7,8,9,10,11,12]
        L = [0,0,0,0,0,0,0,0,0,0,0]
        for i in range(10000):
            x = randint(1,7)
            y = randint(1,7)
            if x+y in l:
                e = l.index(x+y)
                L[e] +=1 
        s = sum(L)
        for c in range(len(L)):
            L[c] = str(round((L[c] / s) * 100,2)) + '%'
        print(L)

    def exercise10():
        l = [1,2,3,4,5,6,7,8,9,10]
        L = []
        for i in range (len(l)):
            L.append(l[i-1])
        print(L)

    def exercise11():
        L =[]
        for i in range(5):
            L.append(1)
            for j in range (i):
                L.append(0)
        print(L)

    def exercise12():
        from random import randint
        L =[]
        for i in range(20):
            L.append(randint(0,1))
        
        o = 0
        os = 0
        z = 0
        zs = 0
        for j in range(len(L)):
            if L[j] == 0 :
                o += 1
            else:
                if o > os :
                    os = o
                o = 0
            if L[j] == 1 :
                z += 1
            else:
                if z > zs :
                    zs = z
                z = 0
        
        print(L)
        print("The longest list of 0's =", os)
        print("The longest list of 1's =", zs)
        
    def exercise13():
        l = [1,1,2,3,4,3,0,0]
        L = []
        for i in l:
            if i not in L:
                L.append(i)
        print(L)

    def exercise14():
        unit = [1, 2, 3]
        key = [12, 30.48, 0.333]
        siu = ['inches','centimeters','yards']
        num = eval(input("Enter a lenght in feet: "))
        print("Enter 1 for inches \n Enter 2 for centimeters \nEnter 3 for yards")
        convert = eval(input("Enter a unit to convert to: "))
        if convert in unit:
            e = unit.index(convert)
            result = num * key[e]
            print(num,"feets converts:",result,siu[e]) 
        else:
            print("Enter a valid convertion")


    def exercise15():
        pass