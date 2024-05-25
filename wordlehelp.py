print("This program searches words based on the letters revealed. Press enter if no more revealed letters left.\n")
NotFirstAttempt = False
answerfound = 'n'
while answerfound != 'y':
    letterslist = []
    greenpositionlist = []
    yellowpositionlist = []
    while True:
        letter = input("Letter (green):") #position known
        if letter == '':
            break
        position = int(input("Position (0-4):"))
        letterslist.append(letter)
        greenpositionlist.append(position)

    print()
    exist = []
    while True:
        letter = input("Letter (yellow):") #only existence known
        if letter == '':
            break
        position = int(input("Position (0-4):"))
        exist.append(letter)
        yellowpositionlist.append(position)

    print()
    absent = []
    while True:
        letter = input("Letter (grey):") #Absence known
        if letter == '':
            break
        absent.append(letter)

    if NotFirstAttempt == False:
        answer1 = [] #collect all 5 letter words
        file = open('5 letter words.txt','r')
        for line in file:
            answer1.append(line.strip())
        file.close()

    answer2 = [] #filter out based on green letters
    for i in range(len(answer1)):
        correct = True
        for j in range(len(letterslist)):
            if answer1[i][greenpositionlist[j]] != letterslist[j]:
                correct = False
        if correct == True:
            answer2.append(answer1[i])

    answer3 = [] #filter out based on yellow letters
    for i in range(len(answer2)):
        correct = True
        for j in range(len(exist)):
            if exist[j] not in answer2[i]:
                correct = False
            if answer2[i][yellowpositionlist[j]] == exist[j]:
                correct = False
        if correct == True:
            answer3.append(answer2[i])

    answer4 = [] #filter out based on grey letters
    for i in range(len(answer3)):
        correct = True
        for j in range(len(absent)):
            if absent[j] in answer3[i]:
                correct = False
        if correct == True:
            answer4.append(answer3[i])

    print()
    for i in range(len(answer4)):
        print(answer4[i])
    answerfound = input("Have you gotten the answer (y/n)?")
    NotFirstAttempt = True
    for i in range(len(answer1)):
        answer1.pop(0)
    for i in range(len(answer4)):
        answer1.append(answer4[i])



    
    
