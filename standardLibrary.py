from datetime import datetime, date, time
import math

# dattetime
today = datetime.now()
print(today)
print(datetime.date(today))
print(datetime.time(today))
print(datetime.ctime(today))
print(datetime.utcnow())
print(datetime.timestamp(today))
print(datetime.fromtimestamp(datetime.timestamp(today)))

date1 = date(2019, 7, 14)
time1 = time(14, 14, 14)
print(datetime.combine(date1, time1))

print(datetime.strptime("12/2/18 20:59", '%d/%m/%y %H:%M'))

print(today.strftime("%Y年%m月%d日 %H:%M:%S %p"))

# math
# 内置
print(round(7.54))
number1 = (1, 2, 3)
number2 = (1.1, 2.2, 3.3)
print(sum(number1))
print(sum(number2))
# math库
print(math.trunc(7.54))
print(math.ceil(7.54))
print(math.fsum(number1))
print(math.fsum(number2))
