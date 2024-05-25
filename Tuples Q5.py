def findExtremeDivisors(n1,n2):
    smaller = min(n1,n2)
    minVal,maxVal = (None,None) #initialise values to be none
    for i in range(1,smaller + 1):
        if n1%i == 0 and n2%i == 0:
            if minVal == None or minVal > i:
                minVal = i
            if maxVal == None or maxVal < i:
                maxVal = i
    return (minVal,maxVal)

print(findExtremeDivisors(18,30))
print(findExtremeDivisors(2,4))
print(findExtremeDivisors(100,200))
                
    
    
    
