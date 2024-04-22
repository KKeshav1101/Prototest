def test():
    import csv
    import random
    qbfile=open("Question Bank.csv",'r',newline='')
    reader=csv.reader(qbfile)
    enteredoplist=[]
    eqmathlist=[]
    eqphylist=[]
    eqchemlist=[]
    mqlist=[]
    hqlist=[]
    anslist=[]
    marklist=[]
    for row in reader:
        if row[8].lower()=="easy" and (row[1].lower()=="mathematics" or row[1].lower()=="maths" or row[1].lower()=="math"):
            eqmathlist.append([row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])
        elif row[8].lower()=="easy" and row[1].lower()=="physics":
            eqphylist.append([row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])
        elif row[8].lower()=="easy" and row[1].lower()=="chemistry":
            eqchemlist.append([row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])
        elif row[8].lower()=="moderate":
            mqlist.append([row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])
        elif row[8].lower()=="hard":
            hqlist.append([row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])
    easyq=random.sample(eqmathlist,2)+random.sample(eqphylist,2)+random.sample(eqchemlist,2)#random questions chosen from easy list
    modq=random.sample(mqlist,3)#random questions chosen from moderate list
    hardq=random.sample(hqlist,3)#random questions chosen from hard list
    qpaper=easyq+modq+hardq #list containing all the questions in the test
    print("TEST")
    print('''TEST INSTRUCTIONS:
1.The test contains 10 MCQs each of 1 mark.
2.THERE IS NO NEGATIVE MARKING
3.Questions (1-6) are rated easy by the teacher
4.Questions (7-9) are rated moderate by the teacher
5.Question (10-12) are rated hard by the teacher
6.Type only the option letter (A/B/C/D) in the appropriate place for answering and click enter.You will have to attempt questions one by one only.
7.After moving on from a question, it wont be possible to return and change the answer.
8.After entering answer, do check if the answer is valid before pressing enter for the next question, invalid answers will be rendered null and are given 0 marks
ALL THE BEST :)''')
    start=input("press ENTER when ready to start the test")
      
    for i in qpaper:
        print(str(qpaper.index(i)+1)+".",i[1])
        print(i[2],i[3],i[4],i[5],sep="\n")
        attempt=input("Enter an appropriate option(A/B/C/D) :")
        if attempt.upper() not in "ABCD":
            print("Valid option not entered no marks given for the question")
        enteredoplist.append(attempt)
        anslist.append(i[6])
    #test analysis    
    for i in range(len(enteredoplist)):
        if enteredoplist[i].upper()==anslist[i].upper():
            marklist.append(1)
        else:
            marklist.append(0)
    easycorrect=0
    modcorrect=0
    hardcorrect=0
    phycorrect=0
    chemcorrect=0
    mathcorrect=0
    totalphy=0
    totalmath=0
    totalchem=0
    for i in qpaper:
        if i[7].lower()=="easy":
            if enteredoplist[qpaper.index(i)]==anslist[qpaper.index(i)]:
                easycorrect=easycorrect+1
        elif i[7].lower()=="moderate":
            if enteredoplist[qpaper.index(i)]==anslist[qpaper.index(i)]:
                modcorrect=modcorrect+1
        elif i[7].lower()=="hard":
            if enteredoplist[qpaper.index(i)]==anslist[qpaper.index(i)]:
                hardcorrect=hardcorrect+1
        if i[0].lower()=="physics":
            totalphy=totalphy+1
            if enteredoplist[qpaper.index(i)]==anslist[qpaper.index(i)]:
                phycorrect=phycorrect+1
        elif i[0].lower()=="chemistry":
            totalchem=totalchem+1
            if enteredoplist[qpaper.index(i)]==anslist[qpaper.index(i)]:
                chemcorrect=chemcorrect+1
        elif i[0].lower()=="mathematics" or i[0].lower()=="math" or i[0].lower()=="maths":
            totalmath=totalmath+1
            if enteredoplist[qpaper.index(i)]==anslist[qpaper.index(i)]:
                mathcorrect=mathcorrect+1
        

    print("%15s"%"Your Answer","%15s"%"Correct Answer","%15s"%"Marks Obtained")
    print("="*60)
    for i in range(len(enteredoplist)):
        print("%15s"%enteredoplist[i],"%15s"%anslist[i],"%15s"%marklist[i])
    total=(sum(marklist)/len(marklist))*100
    print("Total :",total,"%")

    print("DIFFICULTY WISE ANALYSIS")
    print("Number of easy questions answered correctly (out of 6) :",easycorrect)
    print("Number of moderate questions answered correctly (out of 3):",modcorrect)
    print("Number of hard questions answered correctly (one question):",hardcorrect)

    print("SUBJECT WISE ANALYSIS")
    print("Physics :",phycorrect/totalphy*100,"%")
    print("Chemistry :",chemcorrect/totalchem*100,"%")
    print("Mathematics :",mathcorrect/totalmath*100,"%")

    exit=input("PRESS ENTER TO LEAVE PAGE")
    qbfile.close()
