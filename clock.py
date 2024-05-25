import datetime
from datetime import timedelta, date

x = datetime.datetime.now()
print("Entire date =", x)
print("Year =", x.year)
print("Month =", x.month)
print("Day =",x.day)

endDate = date.today() + timedelta(days = 10)
print("End date =", endDate)

x = datetime.datetime(2020,5,17)
print(x.year)

aDate = "21 June 2021"
x = datetime.datetime.strptime(aDate, "%d %B %Y")
print(x)

aDate = "21/06/2021"
x = datetime.datetime.strptime(aDate, "%d/%m/%Y")
print(x)
