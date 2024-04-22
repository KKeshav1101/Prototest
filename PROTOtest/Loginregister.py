import Qadd
import MAINPAGE
import testpg
import mysql.connector as ms

mycon=ms.connect(host="localhost",user="root",passwd="keshav1211",database="prototest")
mycurs=mycon.cursor()
mycurs.execute("select * from student")
sdata=mycurs.fetchall()
mycurt=mycon.cursor()
mycurt.execute("select * from teacher")
tdata=mycurt.fetchall()


print('''WELCOME TO PROTOtest.
If this is your first time here , enter REGISTER
Already signed up , enter LOGIN ''')

def starting():
    firsttime=input()
    if firsttime.lower()=='register':
        loginid=input('Enter your login id (only 10 characters at max) ')
        sort=input('Enter if you are a teacher or a student ')
        pw=int(input('''Enter 5 digit password (Make sure to not forget)'''))
        if sort.lower()=='student':
            mycurs.execute("insert into student values('{0}','{1}')".format(loginid,pw))
            mycon.commit()
        elif sort.lower()=='teacher':
            mycurt.execute("insert into teacher values('{0}','{1}')".format(loginid,pw))
            mycon.commit()
            
        print('You have successfully registered.')
        print('Enter \'login\' to proceed.')
        starting()
        
    elif firsttime.lower()=='login':
        checklogin=input('please enter your id')
        checkpw=int(input('enter your password'))
        print(sdata) 
        r=[]
        r1=[]
        for row in sdata:
            r.append(row)
        for t in tdata:
            r1.append(t)
        for i in r:
            if len(i)!=0:
                if i[0]==checklogin:
                    if i[1]==checkpw:
                            print('Student Page')
                            MAINPAGE.student()#expand
                            break
                    else:
                        print('Please check your password')
        for k in r1:
            if len(k)!=0:
                if k[0]==checklogin:
                    if k[1]==checkpw:
                        print('Teacher Page')#expand
                        MAINPAGE.teacher()
                        break
                    else:
                        print('Please check your password ')
starting()
