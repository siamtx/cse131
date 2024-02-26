## this is me playing with some functions.

#for letter in "hello":
##    print(letter)
#mylist = ['bill',  'tim', 'patal', 'suzy']
#for item in mylist:
#    print(mylist[1])


#i = 1
#while i <= 50:
#    print(i)
#    i = i + 2


#while True:
 #   print("I am stuck in a loop!!")


## Functions
#print('Hello, readers!')

#myLength = len('hello')
#print(myLength)

#def say_hi():
#    print('Hi!')
#
#say_hi()

"""
def green():
    response = input("Is the moon green?  ")


def choose():
    if input == 'yes':
        print("You win!")
    if input == 'no':
        print("The sky is crying!!!") 
          

green()
choose()
"""

def say_hi(name):
    if name == ' ':
        print("You didn't enter your name!")
    else:
        print("Hi there!")
        for letter in name:
             print(letter)

name = input("Your name:  ")
say_hi(name)