##Different methods for importing library in python
##Author : Akshay Sankle

####----1-----#####
from datetime import date
today = date.today()
print("1st Today's date:", today)

####----2-----#####
from datetime import date
print("2nd Today's date:", date.today())

####----3-----#####
import datetime
today = datetime.date.today()
print("3rd Today's date:", today)

####----4-----#####
from datetime import date
print("4th Today's date:",date.today())

####----5-----#####
from datetime import*
print("5th Today's date:", date.today())


#Output:-

#1st Today's date: 2020-12-14
#2nd Today's date: 2020-12-14
#3rd Today's date: 2020-12-14
#4th Today's date: 2020-12-14
#5th Today's date: 2020-12-14
