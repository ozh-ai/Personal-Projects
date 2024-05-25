#Task 1.1
print("Task 1.1")
print("")

file = open('Rainfall_mth.csv','r') #open month file
monthlist = []
for line in file:
    monthlist.append(line.strip().split(','))
monthlist.pop(0)
# print(monthlist)
file.close()

print(" {:^5} | {:^20} ".format('Year','Total Annual Rainfall (millimetres in 1 d.p.)')) #heading
for year in range(1984,2015):
    yearlyrainfall = 0
    for i in range(len(monthlist)):
        if year == int(monthlist[i][0][0:4]):
            yearlyrainfall = yearlyrainfall + float(monthlist[i][1])
    print(" {:^5} | {:^20} ".format(year, yearlyrainfall))
            

#Task 1.2
print("")
print("Task 1.2")
print("")

file = open('Rainfall_mth.csv','r') #open month file
monthlist = []
for line in file:
    monthlist.append(line.strip().split(','))
monthlist.pop(0)
# print(monthlist)
file.close()

file = open('Rainfall_day.csv','r') #open days file
daylist = []
for line in file:
    daylist.append(line.strip().split(','))
daylist.pop(0)
print(daylist)
file.close()

year = int(input("Enter the year:")) #input year
if year<2009 or year>2014:
    print("ERROR")
else:    
    yearlyrainfall = 0  #find total rainfall
    for i in range(len(monthlist)):
        if year == int(monthlist[i][0][0:4]):
            yearlyrainfall = yearlyrainfall + float(monthlist[i][1])
    days = 0   #find number of days it rained
    for i in range(len(daylist)): 
        if year == int(daylist[i][0][0:4]):
            days = days + float(daylist[i][1])
    average = yearlyrainfall/days
    print("Average rainfall for a rainy day in",year,"is",average,"millimetres.")
    
        

    
    
