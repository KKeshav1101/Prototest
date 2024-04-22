import csv
def add():
    f=open("Question Bank.csv","r",newline='')
    r=csv.reader(f)
    l=[]
    for i in r:
        l.append(i)
        qid=eval(i[0]+"+1")   
    f.close()
    f=open("D:\School\Computer Science-Project\PROTOtest\Question Bank.csv","w",newline='')
    w=csv.writer(f)
    n=int(input("Enter number of questions to be added :"))
    for i in range(n):
        sub=input("Enter Subject [Physics,Chemistry,Math]  :")
        q=input("Enter the question in detail :")
        op1=input("Enter option A (LABEL OPTION AS A) WHILE ENTERING):")
        op2=input("Enter option B (LABEL OPTION AS B) WHILE ENTERING):")
        op3=input("Enter option C (LABEL OPTION AS C) WHILE ENTERING):")
        op4=input("Enter option D (LABEL OPTION AS D) WHILE ENTERING):")
        correct=input("Enter the correct option (A/B/C/D) :")
        diff=input("Enter difficulty according to your judgement (\"Easy\",\"Hard\",\"Moderate\") :")
        print(qid,"IS THE Q.ID OF THE QUESTION")
        l.append([qid,sub,q,op1,op2,op3,op4,correct,diff])
        qid=qid+1
    w.writerows(l)
    print("<<<<< Successfully added",n,"question(s) :) >>>>>")
    f.close()
    

def view():
    f=open("Question Bank.csv",'r',newline='')
    r=csv.reader(f)
    print("Question Bank")
    print("%10s"%"Q.ID","%15s"%"Subject","%20s"%"Question","%30s"%"Difficulty")
    print("="*100)
    for i in r:
        print("%10s"%i[0],"%15s"%i[1],"%20s"%i[2][:20:]+"...","%30s"%i[8])
    f.close()


def delete():
    f=open("Question Bank.csv",'r',newline='')
    r=csv.reader(f)
    l=[]
    for i in r:
        l.append(i)
    id=int(input("Enter Q.ID of question to be removed :"))
    k=0
    for j in l:
        if j[0]==str(id):
            l.remove(j)
            k=k+1
    if k==0:
        print("The entered QID doesnt exist")
   
    f.close()
    f=open("D:\School\Computer Science-Project\PROTOtest\Question Bank.csv",'w',newline='')
    w=csv.writer(f)
    w.writerows(l)
    print("<<<< Question Successfully Removed >>>>")
    f.close()


