from datetime import datetime as dt,date
from dateutil.relativedelta import relativedelta

class MyAge:
    def __init__(self,date_of_birth,myname):
        self.__date_of_birth = dt.strptime(date_of_birth,'%Y-%m-%d')
        self.__myname=myname
        self.__my_age_years=relativedelta(date.today(),self.__date_of_birth).years
        print(self.__date_of_birth)

    def show_me_my_age(self):
        return f"{self.__myname}, you are young, only {self.__my_age_years} years old"


age = MyAge("1991-10-30","Onkar")
print(age.show_me_my_age())
