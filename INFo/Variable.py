a = "Hello Sony Nguyen"
print(str.splitlines(a))
print(str.isnumeric(a))
number = "1,2,3,4,5"
print(number)
print(str.isnumeric(number))
b = 2
c = 3
print(str(b)+str(c))
chuthuong = "hôm nay là ngày thứ hai tôi học Python"
CHUHOA = str.upper(chuthuong)
print(CHUHOA)
# lấy toàn bộ nội dung của thư viện decimal
# từ thư viện decimal -> import mọi thứ (*) vào
from decimal import*
# lấy tối đa 30 chữ số phần nguyên và phần thập phân Decimal
getcontext().prec = 10
d = (Decimal(10)/3)
print(d)
print (type(d))

f=10/3
print(f)
print(type(f))