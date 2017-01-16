#-*- coding:utf-8 -*-
import datetime

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
        month = t%12 if t%12 else 12
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


def _add_month(year, month, month_count):
    t = month + month_count
    if t > 12:
        year = year + t/12
        month = t%12 if t%12 else 12
    else:
        month = t
    return year,month

def getJIKUANDate(start_date, month_count):
    result = []
    date_list = start_date.split('-')
    year = int(date_list[0])
    month = int(date_list[1])
    day = int(date_list[2])
    if day == 1:
        for i in range(1, month_count-1):
            after_year,after_month = _add_month(year, month, i)
            one_date = '%s-%s-%s' % (after_year,after_month,10)
            result.append(one_date)
        after_year,after_month = _add_month(year, month, month_count)
        if after_month in [1,3,5,7,8,10,12]:
            after_day = 31
        elif after_month == 2:
            after_day = 29 if isrun(after_year) else 28
        else:
            after_day = 30
        one_date = '%s-%s-%s' % (after_year,after_month,after_day)
        result.append(one_date)
    elif day <= 10:
        for i in range(1, month_count):
            after_year,after_month = _add_month(year, month, i)
            one_date = '%s-%s-%s' % (after_year,after_month,10)
            result.append(one_date)
        after_year,after_month = _add_month(year, month, month_count)
        after_day = day-1
        one_date = '%s-%s-%s' % (after_year,after_month,after_day)
        result.append(one_date)
    elif day<26:
        for i in range(1, month_count):
            after_year,after_month = _add_month(year, month, i)
            one_date = '%s-%s-%s' % (after_year,after_month,25)
            result.append(one_date)
        after_year,after_month = _add_month(year, month, month_count)
        after_day = day-1
        one_date = '%s-%s-%s' % (after_year,after_month,after_day)
        result.append(one_date)
    else:
        for i in range(2, month_count):
            after_year,after_month = _add_month(year, month, i)
            one_date = '%s-%s-%s' % (after_year,after_month,10)
            result.append(one_date)
        after_year,after_month = _add_month(year, month, month_count)
        after_day = day-1
        if after_month == 2 and after_day>28:
            after_day = 29 if isrun(after_year) else 28
        one_date = '%s-%s-%s' % (after_year,after_month,after_day)
        result.append(one_date)
    return result

def mathsum(into):
    return int('%d' % into)

def getJIEKUANSum(YFDate, buy_sum, buy_date, year_rate, buy_deadline):
    month_money = mathsum(buy_sum * year_rate /12)
    total_menory = mathsum(buy_sum * year_rate * buy_deadline /12)
    t = len(YFDate) - 2
    start_list = buy_date.split('-')
    end_list = YFDate[0].split('-')
    start_list = map(int, start_list)
    end_list = map(int, end_list)
    d1 = datetime.datetime(start_list[0],start_list[1],start_list[2])
    d2 = datetime.datetime(end_list[0], end_list[1], end_list[2])
    days = (d2-d1).days
    first_money = mathsum(buy_sum * year_rate * days / 365)
    last_money = mathsum(total_menory - first_money - month_money*t + buy_sum)
    r = [first_money] + [month_money]*t + [last_money]
    return r
