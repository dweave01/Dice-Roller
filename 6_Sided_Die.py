'''
Created on Aug 31, 2020

@author: Daniels
'''
import random

def RollDice():
    return random.randrange(1,7)
    
def PrintDice(r):
    
    if r == 1:
        print ("""
        _________
       |         |
       |         |
       |    *    |
       |         |
       |_________|""")
        
    elif r == 2:
        print ("""
        _________
       |         |
       |     *   |
       |         |
       |   *     |
       |_________|""")
        
    elif r == 3:
        print ("""
        _________
       |         |
       |      *  |
       |    *    |
       |  *      |
       |_________|""")
        
    elif r == 4:
        print ("""
        _________
       |         |
       |  *   *  |
       |         |
       |  *   *  |
       |_________|""")
    
    elif r == 5:
        print ("""
        _________
       |         |
       |  *   *  |
       |    *    |
       |  *   *  |
       |_________|""")
        
    elif r == 6:
        print ("""
        _________
       |         |
       |  *   *  |
       |  *   *  |
       |  *   *  |
       |_________|""")


#PrintDice(RollDice())


def toBool (x):
    if x.lower() == "yes":
        x = True
    else:
        x = False
    return x

def main():
    UserName = input("Hello, Welcome to a Simple 6 sided die project, What is your name?\n")
    YesOrNo = input("Welcome " + UserName + " would you like to roll a die?\n")
    Answer = toBool(YesOrNo)
    while (Answer):
        print("Rolling now...")
        PrintDice(RollDice())
        YesOrNo = input("Would you like to roll again?")
        Answer = toBool(YesOrNo)
    print("Thank you for playing "+ UserName + ", have a good day :)")


if __name__ == '__main__':
    main()
