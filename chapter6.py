#This is based on the chapters in 'A Practical Introduction to Python Programming Heinold (PDF)
#Chapter 6 - Strings

class section10:
    def example1():
        print('\n'*9)

    def example2():
        s = input('Enter some text: ')
        for i in range(len(s)):
            if s[i]=='a':
                print(i)

    def example3():
        s = input('Enter some text: ')
        doubled_s = ''
        for c in s:
            doubled_s = doubled_s + c*2
        print(doubled_s)

    def example4():
        name = input('Enter your name: ')
        for i in range(len(name)):
            print(name[:i+1], end=' ')

    def example5():
        s = input("Enter some text: ")
        s = s.lower()
        for c in ',.;:-?!()\'"':
            s = s.replace(c, '_')
        print(s)

    def example6():
        s = input('Enter your decimal number: ')
        print(s[s.index('.')+1:])

    def example7():
        from math import floor
        num = eval(input('Enter your decimal number: '))
        print(num - floor(num))

    def example8():
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        key = 'xznlwebgjhqdyvtkfuompciasr'
        secret_message = input('Enter your message: ')
        secret_message = secret_message.lower()
        for c in secret_message:
            if c.isalpha():
                print(key[alphabet.index(c)],end='')
            else:
                print(c, end='')

            
class section11:
    def exercise1():
        s = input("Enter a string: ")
        print("(a) The lenght of the string is", len(s))
        print("(b) The string repeated 10 times: ")
        print('\t',(s + ' ')*10)
        print("(c) The first character of the string:",s[0])
        print("(d) The first three characters of the string:", s[ : 3])
        print("(e) The last three characters of the string:", s[-3 : ])
        print("(f) The string backwards:",s[::-1])
        if len(s) > 7 :
            print("(g) The seventh character of the string is:", s[7])
        else:
            print("(g) The string is less than seven characters")

        print("(h) The string wothout the first and last characters:", s[1:-1])
        print("(i) The string all in Upper Case:",s.upper())
        new_s = ' '
        new_s1 = ' '
        for c in s:
            if c == 'a':
                new_s = s.replace(c,'e')
            #if c.isalpha():
            new_s1 = s.replace(c,' ')
        print("(j) The string with all 'a' repalced with an 'e':", new_s)
        print("(k) The string with all characters repalced with a space ' ':", new_s1,'.')

    def exercise2():
        s = input("Enter a string: ")
        count = 0
        for c in s:
            if c == ' ':
                count +=1
        print("There are estimatedly",count+1,"words in your string")
    
    def exercise3():
        f = input("Enter a formula: ")
        open_count = 0
        close_count = 0 
        for c in f:
            if c == '(':
                open_count +=1
            if c == ')':
                close_count +=1
        if open_count < close_count:
            print("Your formulla is missing some opening parentheses")
        elif open_count > close_count:
            print("Your formulla is missing some closing parentheses")
        elif open_count == close_count:
            print("Your formulla has equal number of parenthesss.")

    def exercise4():
        w = input("Enter a word: ")
        count = 0
        for c in w:
            for  v in 'aeiou':
                if c == v :
                    count +=1
        if count > 0:
            print("There are", count, "vowls in your word.")
        else:
            print("There are no vowls in your word.")
    
    def exercise5():
        s = input("Enter a string: ")
        new_s = s[:1] + '*' + s[2:] + '!!!'
        print(new_s)
    
    def exercise6():
        s = input("Enter a string: ")
        new_s = s.lower()
        for c in new_s:
            if c == '.' or c == ',':
                new_s = new_s.replace(c,'')
        print(new_s)

    def exercise7():
        w = input("Enter a word: ")
        r = w[::-1]
        if w == r :
            print("The word is a palindrome")
        else:
            print("The word is NOT a palindrome")
        
    def exercise8():
        num = eval(input("how email addresses will you enter? "))
        s_count = 0
        p_count = 0
        for e in range(num):

            s = input('Enter an address: ')
            i = 0
            for j in range(len(s)):
                if s[j] == '@':
                    i = j
            if s[i: ] == "@student.college.edu":
                s_count +=1
            elif s[i: ] =="@prof.college.edu":
                p_count +=1
        if s_count == num:
            print("All the addresses are student addresses")
        else:
            print("There were some",s_count,"student addresses entered")
            print("There were some",p_count,"professor addresses entered")

    def exercise9():
        num = eval(input("Enter a number: "))
        for i in range(1,num+1):
            print(' '*i, i)

    def exercise10():
        s = input("Enter a string: ")
        for i in range(len(s)):
            print(s[i]*2,)

    def exercise11():
        s = input("Enter a string: ")
        print(s[:s.index('a')+1])
        print(s[s.index('a')+1:])
    
    def exercise12():
        w = input("Enter a word: ")
        print(w[0].lower(), end='')
        for i in range(1,len(w)):
            if i % 2 != 0:
                print(w[i].upper(), end='')
            else:
                print(w[i].lower(), end='')
        
    def exercise13():
        print("Enter two strings and of the same length")
        s1 = input("Enter the first string: ")
        s2 = input("Enter the secind string: ")
        if len(s1) == len(s2):
            for i in range(len(s1)):
                print(s1[i],end='')
                print(s2[i],end='')
        else:
            print("The strings are not of the same lenght. Try again")


    def exercise14():
        name = input("Enter your full name: ")
        check = 0
        for i in range(len(name)):
            if i == 0 and i != ' ':
                print(name[0].upper(), end='')
                
            elif i > 0 :
                if name[i] == ' ':
                    check = i + 1
                    print(name[i], end='')
                elif i == check :
                    print(name[i].upper(), end='')
                else:
                    print(name[i], end='')
                
    def exercise15():
        name = input("Enter your name: ")
        verb =  input("Enter a verb: ")
        adjetive = input("Enter an adjetive: ")
        print("Hi i'm",name,",and always",adjetive,"to",verb,"")

    def exercise16():
        fname = input("Enter your first name: ")
        lname = input("Enter your last name: ")
        print("Dear ", fname, lname,",", sep='')
        print("I am pleased to offer you our new Platinum Plus Rewards card")
        print("at a special introductory APR of 47.99%. ", fname, " ,an offer", sep='')
        print("like this does not come along every day, so I urge you to call")
        print("now toll-free at 1-800-314-1592. We cannot offer such a low")
        print("rate for long, ", fname, ", so call right away.",sep='')

    def exercise17():
        a = "abcdefghijklmnopqrstuvwxyz"
        for i in range(26):
                print(a[i:] + a[:i])
            
    def exercise18a():
        s = input("Enter a string: ")
        l = input("Enter a letter: ")
        found = False
        for i in range(len(s)):
            if s[i] == l :
                found = True
                
        if found == True:
            print("The letter",l,"appears in your string")
        else:
            print("The letter",l,"does NOT appear in your string")

    def exercise18b():
        s = input("Enter a string: ")
        l = input("Enter a letter: ")
        n = ''
        found = False
        for i in range(len(s)):
            if s[i] == l :
                found = True
                n += l
        if found == True:
            print("The letter",l,"appears",len(n)," times in your string")
        else:
            print("The letter",l,"does NOT appear in your string")

    def exercise18c():
        s = input("Enter a string: ")
        l = input("Enter a letter: ")
        n = 0 
        found = False
        for i in range(len(s)):
            if s[i] == l :
                found = True
                n = i
                break
                
        if found == True:
            print("The first occureance of the letter",l,"is at index",n,"your string")
        else:
            print("The letter",l,"does NOT appear in your string")

    def exercise19():
        num = input("Enter a large integer: ")
        num = num[::-1]
        new_num = ' '
        for i in range(len(num)):
            if i == 0:
                new_num += num[i]
            elif( i > 0):
                if len(new_num) % 4 == 0 :
                    new_num += ','
                    #print(",", end='')
                else:
                    new_num += num[i]
                    #print(num[i], end='')
        print(new_num[::-1])

    def exercise20():
        pass

    def exercise21():
        from random import randint
        w = input("Enter a word that does not contain repeative characters eg(beans): ")
        next_c = w[randint(0,len(w)-1)]
        new_w = ''
        while len(new_w) <= len(w):
            if next_c in new_w and (next_c in len(w)) :
                next_c = w[randint(0, len(w)-1)]
                #print("next =",next_c)
            else:
                new_w += next_c
                if len(new_w) == len(w):
                    break
                    
                #print("new_w=",new_w)
        print(new_w)

    def exercise22a():
        s = input("Enter a string to encrypt: ")
        even_s = s[::2]
        odd_s = s[1::2]
        print("the encrypted string is",even_s + odd_s)
                
    def exercise22b():
        s = input("Enter a string to dencrypt: ")
        l = len(s)/2
        l = int(l)
        if len(s) % 2 == 0:
            slice1 = s[:l]
            slice2 = s[l:]
        else:
            slice1 = s[:l+1]
            slice2 = s[l+1:]
        print("The decrypted string is ",end='')
        for i in range((len(s))):
            if i < len(slice1):
                print(slice1[i],end='')
            if i < len(slice2):
                print(slice2[i],end='')

    def exercise23a():
        s = input("Enter a string to encrypt: ")
        first_s = s[::3]
        second_s = s[1::3]
        third_s = s[2::3]
        print("the encrypted string is:",first_s + second_s + third_s)
    
    def exercise23b():
        s = input("Enter a string to dencrypt: ")
        l = len(s) / 3
        l = int(l)
        if int(len(s)) % 3 == 0:
            slice1 = s[:l]
            slice2 = s[l:int(len(slice1)*2)]
            slice3 = s[int(len(slice2)*2):] 
        else:
            slice1 = s[:l+1]
            slice2 = s[l+1:]
            slice3 = s[int(len(slice2))+1:] 
        for i in range(len(s)):
            if i < len(slice1):
                print(slice1[i],end='')
            if i < len(slice2):
                print(slice2[i],end='')
            if i < len(slice3):
                print(slice3[i],end='')

    def exercise23c():
        s = input("Enter a string to encrypt: ")
        if len(s) % 2 != 0 :
            s += '*'
        num = eval(input("Enter how many parts to break it into: "))
        encryp_s = ''
        for i in range(num):
            encryp_s += s[i::num]
            #print("Slice",i,s[i::num])
        print("The encrypted string is:",encryp_s)

    def exercise23d():
        s = input("Enter a string to decrypt: ")
        num = eval(input("Enter how many parts it has been boken into: "))
        step = len(s) // num
        step = int(step)
        print("Step -",step)
        for j in range(step):
            if len(s)%2 == 0:
                print(s[j::step], end='')
            else:
                print("Invalid encripted message")
            
    def exercise24():
        e = input("Enter an exponential expresion eg: x^3 : ")
        num = e[2:]   
        num = int(num)   
        print("The derivative is: ",str(num),e[0],"^",str(num-1), sep='') 

    def exercise25():
        e = input("Enter an algebraic expresion: ")
        new_e =''
        for i in range(len(e)) :
            if e[i] == '(':
                new_e += e[:i] + '*' +e[i:]
        print(new_e)