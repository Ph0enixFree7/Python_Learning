import datetime
mytime = datetime.time(15,3,1)
print(mytime)
today = datetime.date.today()
print(today)
print(today.ctime())
mydatetime = datetime.datetime(2021,10,3,14,35,24)
mydatetime = mydatetime.replace(year = 2020)
print(mydatetime)
date1 = datetime.date(2021,11,3)
date2 = datetime.date(2020,11,3)
print(date1 - date2)
datetime1 = datetime.datetime(2021,11,3,22,0)
datetime2 = datetime.datetime(2020,11,3,12,0)
print(datetime1 - datetime2)