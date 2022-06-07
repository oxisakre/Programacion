import datetime
 
from datetime import timedelta 
 
d=int(input("ENTER THE DAY : "))
 
m=int(input("ENTER THE MONTH : "))
 
y=int(input("ENTER THE YEAR : "))
     
 
# format given date
gDate = datetime.datetime(y, m, d) 
print("Given date is: ", gDate) 
   
# Yesterday date 
yesterday = gDate + timedelta(days = 1) 
print("Next date will be : ", yesterday) 