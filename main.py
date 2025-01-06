'''from datetime import *


date_today=datetime.today()
interval=timedelta(days=45)


print(current_day-interval)
print(current_day)
print(current_day+interval)
count_days=(current_day-interval)-(current_day+interval)
print(count_days.days)'''
from datetime import *

current_day=datetime.now()

datetime_string='1970:01:01'
print (datetime.strptime(datetime_string,'%Y:%m:%d'))
#print (current_day.strftime('%Y-%m-%d'),current_day)
