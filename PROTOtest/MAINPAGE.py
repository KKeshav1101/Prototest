import csv
import Qadd
import testpg
#Teacher-Side window
def teacher():
    while True:
        op=int(input('''Welcome to PROTOtest,
TEACHER MENU
CHOOSE WHAT YOU WOULD LIKE TO DO
1.ADD A QUESTION
2.VIEW THE QUESTION BANK (RECOMMENDED BEFORE REMOVING A QUESTION)
3.DELETE A QUESTION
4.EXIT'''))
        if op==1 or op==2 or op==3 or op==4:
            if op==1:
                Qadd.add()
            if op==2:
                Qadd.view()
            if op==3:
                Qadd.delete()
            if op==4:
                print("Have a nice day :)")
                break
        else:
            print("Pls enter a valid option")
            continue

#Student-Side window
def student():
    while True:
        op=input('''Welcome to PROTOtest,
TEST Yourself in JEE Concepts right away!
Type PROTOTEST to take up a test now!!!!
Type EXIT if you want to Exit page''')
        if op=='PROTOTEST':
            testpg.test()
        elif op.upper()=="EXIT":
            print("Have a nice day :)")
            break
        else:
            print("Make sure you type the exact letters 'PROTOTEST'(case sensitive) if you wanted to take up a test")
            continue
            
    
