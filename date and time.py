import datetime
datetimeobj = datetime.datetime.now()
print(datetimeobj)
print('Year : ',datetimeobj.year)
print('Month : ',datetimeobj.month)
print('day : ',datetimeobj.day)
print('Hour : ',datetimeobj.hour)
print('minute : ',datetimeobj.minute)
print('second : ',datetimeobj.second)
print('microsecond : ',datetimeobj.microsecond)
################################################
import datetime
data = datetime.datetime.now()
print('Day short from : ',data.strftime('%a'))
print('Day full from : ',data.strftime('%A'))
print('month short from : ',data.strftime('%b'))
print('month full from : ',data.strftime('%B'))
print('year short from : ',data.strftime('%y'))
print('year full from : ',data.strftime('%Y'))
print('Day count in week : ',data.strftime('%w'))
print('Day count in month : ',data.strftime('%d'))
print('month count in year : ',data.strftime('%n'))
print('Day count in year : ',data.strftime('%j'))
print('Hour : ',data.strftime('%H'))
print('Hour (0-12) : ',data.strftime('%I'))
print('AM/PM : ',data.strftime('%p'))
print('Minute : ',data.strftime('%M'))
print('Second : ',data.strftime('%S'))
print('microsecond : ',data.strftime('%f'))
print('week count in year : ',data.strftime('%U'))
print('Century : ',data.strftime('%C'))
