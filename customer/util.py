#-*- coding:utf-8 -*-

def isrun(year):
    if year%400 == 0:
        return True
    elif year%4 == 0 and year%100 != 0:
        return True
    else:
        return False
    
def getdate(this_date, after_months):
    date_list = this_date.split('-')
    year = int(date_list[0])
    month = int(date_list[1])
    day = int(date_list[2])
    t = month + after_months
    if t > 12:
        year = year + t/12
        month = t%12
    else:
        month = t
    if day > 1:
        day = day - 1
        if month == 2:
            if isrun(year):
                if day>29:
                    day = 29
            else:
                if day>28:
                    day = 28
    else:
        if month > 1:
            month = month - 1
            if month in [1,3,5,7,8,10,12]:
                day = 31
            elif month == 2:
                day = 29 if isrun(year) else 28
            else:
                day = 30
        else:
            year = year - 1
            month = 12
            day = 31
    return '-'.join([str(year), str(month), str(day)])