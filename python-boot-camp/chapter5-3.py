import datetime
d = datetime.date(2019,9,21)
print (d.year,d.month,d.day)

today = datetime.date.today()
print (today)
print (today.year,today.month,today.day)


birthday = datetime.date(1982,12,7)
delta = today - birthday
print ("Takashi:"+str(delta.days))

birthday = datetime.date(1984,3,21)
delta = today - birthday
print ("Azusa:"+str(delta.days))

birthday = datetime.date(2016,3,3)
delta = today - birthday
print ("Haruno:"+str(delta.days))

birthday = datetime.date(2019,2,18)
delta = today - birthday
print ("Aya:"+str(delta.days))
