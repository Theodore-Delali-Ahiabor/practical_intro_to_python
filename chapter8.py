# This is based on the chapters in 'A Practical Introduction to Python Programming Heinold (PDF)
# Chapter 8 - More with Lists

class Section1:
    def example1(self):
        from random import choice
        names = ['Joe', 'Bob', 'Sue', 'Sally']
        current_player = choice(names)
        print(current_player)
    
    def example2():
        from random import sample
        names = ['Joe', 'Bob', 'Sue', 'Sally']
        team = sample(names, 2)
        print(team)

    def example3():
        from random import choice
        s='abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
        for i in range(10000):
            print(choice(s), end='')
    
    def example4():
        from random import shuffle
        players = ['Joe', 'Bob', 'Sue', 'Sally']
        shuffle(players)
        for p in players:
            print(p, 'it is your turn.')

    def testrun1():
        from string import punctuation
        s = input('Enter a string: ')
        for c in punctuation:
            s = s.replace(c, '')
        s = s.lower()
        L = s.split()
        word = input('Enter a word: ')
        print(word, 'appears', L.count(word), 'times.')

    def testrun2():
        from random import shuffle
        word = input('Enter a word: ')
        letter_list = list(word)
        shuffle(letter_list)
        anagram = ''.join(letter_list)
        print(anagram)

class Section5:
    def example1():
        from random import randint
        L = [randint(1,101) for i in range(50)]
        print(L)

    def example2():
        from random import randint
        l = [randint(1,101) for i in range(50)]
        L = [i*2 for i in l]
        print(L)

    def example3():
        from random import randint
        l = [randint(1,101) for i in range(50)]
        L = [i for i in l if i > 50]
        print(L)


    def example4():
        from random import randint
        l = [randint(1,101) for i in range(50)]
        L = [l.count(i) for i in l]
        print(L)

    def example5():
        from random import choice
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        s = ''.join([choice(alphabet) for i in range(1000)])
        print(s)

    