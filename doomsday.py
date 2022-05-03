import math
# month = [doomsdate, numofdays, doomsdate(leapyear), numofdays(leapyear)]
January = [3,31,4,31]
February = [7,28,1,29]
March = [7,31,7,31]
April = [4,30,4,30]
May = [2,31,2,31]
June = [6,30,6,30]
July = [4,31,4,31]
August = [1,31,1,31]
September = [5,30,5,30]
October = [3,31,3,31]
November = [7,30,7,30]
December = [5,31,5,31]
months = [January, February, March, April, May, June, July, August, September, October, November,December]
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# start from noneday to sixturday
# doomsday 3(4)/1, 28(29)/2, 14/3, 4/4, 9/5, 6/6, 11/7  8/8, 5/9 10/10, 7/11  12/12
# 1800 to 1899 is a Friday
# 1900  to 1999 is a Wednesday
# 2000 to 2099 is a Tuesday
# 2100 to 2199 is a Sunday
#input year,month,date
year = input('Enter a year: ')
month = int(input('Enter a month: '))
while month > 13:
    print('Please input a month within human calendar!!')
    month = int(input('Enter a month: '))
date = int(input('Enter a date: '))
year0_and_1 = int((year[0]+year[1]))
#leap year check
def leap_year():
    check1 = int(year) % 4
    check2 = int(year) % 100
    check3 = int(year) % 400
    if check1 == 0 and check2 != 0:
        return True
    elif check2 == 0 and check3 == 0:
        return True
    else:
        return False
#generating anchor day
modulo_value = year0_and_1 % 4
if modulo_value == 0 :
    anchor_day = 2
elif modulo_value == 1 :
    anchor_day = 0
elif modulo_value == 2 :
    anchor_day = 5
else :
    anchor_day = 3
#generating doomsday
year2_and_3 = int((year[2]+year[3]))
twelve_fits = math.floor(year2_and_3 / 12)
modulo_diff = year2_and_3 % 12
four_fits = math.floor(modulo_diff / 4)
results = anchor_day + twelve_fits + modulo_diff + four_fits
doomsday_day = results % 7
doomsmonth = months[month-1]
if leap_year():
    doomsdate = doomsmonth[2]
else :
    doomsdate = doomsmonth[0]
while doomsdate < date:
    doomsdate += 7
diff_date = doomsdate - date
while diff_date > doomsday_day:
    doomsday_day += 7
the_dday = int(doomsday_day - diff_date)
print('It\'s a %s! ' % days[the_dday])