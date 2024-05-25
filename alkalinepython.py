infile = open("alkaline_metals.txt","r")
alkalineList = []
for line in infile:
    alkalineList.append([line])
print(alkalineList)
infile.close()
