import sys


def step1():
    global num1
    num1 = input("Enter a number (or letter to exit): ")
    if num1.isalpha():
        sys.exit()
    else:
        step2()


def step2():
    global operator
    operator= input("Enter an operator: ")
    if operator == '+' or operator == '-' or operator == '*' or operator == '/':
        step3()
    else:
        print ("Invialid system")
        step2()

def step3():
    global num2
    num2 = input("Enter another number (or letter to exit): ")
    if num2.isalpha():
        sys.exit()
    else:
        step4()

def step4():
    if operator == '+' :
        print ("Result:", format(float(num1.replace(',','.'))+float(num2.replace(',','.')), '.2f'))
    elif operator == '-':
        print ("Result:", format(float(num1.replace(',','.'))-float(num2.replace(',','.')), '.2f'))
    elif operator == '*':
        print ("Result:", format(float(num1.replace(',','.'))*float(num2.replace(',','.')), '.2f'))
    else:
        print ("Result:", format(float(num1.replace(',','.'))/float(num2.replace(',','.')), '.2f'))
    print ("\n")
    step1()


step1()
