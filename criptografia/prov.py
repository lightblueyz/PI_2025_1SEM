import datetime 
from os import system as sys
sys("cls")

def EndDays():
    return str((365-(datetime.date.today()-(datetime.date(int(str(datetime.date.today()).split("-")[0]),1,1))).days/365)*100) 


print(EndDays())

