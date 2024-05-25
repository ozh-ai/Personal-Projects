unbanned = input("Available letters:")
repeatlist = []
while True:
    repeated = input("Repeated letter ('' for no repeats):")
    if repeated == '':
        break
    repeatlist.append(repeated)

while True:
    print("")
    length = int(input("Length:"))
    if length == 0:
        break

    print("")
    print("This program will search words based on revealed letters and its relative position, with the first letter being at position 0.\
     If not applicable, please type ''.")
    print("")
    letterlist = []
    positionlist = []
    while True:
        letter = input("Letter:")
        if letter == '':
            break
        position = int(input("Position:"))
        letterlist.append(letter)
        positionlist.append(position)

    answer1 = [] #filter out all words with incorrect lengths
    if length == 3:
        file = open('3 letter words.txt','r')
    if length == 4:
        file = open('4 letter words.txt','r')
    if length == 5:
        file = open('5 letter words.txt','r')
    if length == 6:
        file = open('6 letter words.txt','r')
    if length == 7:
        file = open('7 letter words.txt','r')
    for line in file:
        answer1.append(line.strip())
    file.close()

    answer2 = [] #filter out all words with incorrect letters
    for i in range(len(answer1)):
        correct = True
        for j in range(len(answer1[i])):
            if answer1[i][j] not in unbanned:
                correct = False
        if correct == True:
            answer2.append(answer1[i])

    answer3 = [] #filter out all words with letters in incorrect positions
    if len(letterlist) == 0:
        answer3 = answer2
    else:
        for i in range(len(answer2)):
            correct = True
            for j in range(len(letterlist)):
                if answer2[i][positionlist[j]] != letterlist[j]:
                    correct = False
            if correct == True:
                answer3.append(answer2[i])

    answer4 = [] #filter out words with repeated letters if applicable
    for i in range(len(answer3)):
        correct = True
        for j in range(len(unbanned)):
            if (unbanned[j] not in repeatlist) and (answer3[i].count(unbanned[j])>1):
                correct = False
        if correct == True:
            answer4.append(answer3[i])

    print("")
    for i in range(len(answer4)):
        print(answer4[i])
        
    
    



    
    





