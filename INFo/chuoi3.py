
# %s
a = "My team %s" %("Sony")
b = "My other team %s" %("Khang")
c = "Today I feel so %s and %s but a little %s. However, I can go to the %s" %("great", "exhausted", "wonderful", "gym")
print(b)
print(a)
print(c)

distance = input("How far did you travel(in miles)?")
time = input("How long did it take you to reach your destination (in hours)?")
where = input("Where were you going?")

speed = round(float(distance)/float(time),2)

print("Oh your journey to %s, you drove at an average speed of %s miles per hour." %(where,speed))
i = '%.2f' %(3.563545) # chỉ lấy 2 số ở phần thập phân
print(i)
o = "%.2f" %(3.9999)  # làm tròn 
print(o)
di = '%d' %(4) # %d thay thế số
print(di)
p = f"xyz" # f"giá trị trong chuỗi"
print(p)
variable = "Nội dung thay thế"
# type của variable có thể là str hoặc int đều được
k = f"Sau đó, mở ngoặc {variable}, giá trị trong biến variable sẽ được thay thế vào chỗ ngoặc nhọn" 
print(k)
# CHÚ Ý F STRING
x = "thành công"
y = "hôm nay"
z = "ngày mai"
f = "thất bại"
s = f'Nếu muốn {x} thì việc {y} chớ để {z}. Kẻ {f} luôn tìm mọi lý do.'
print(s) # chú ý cú pháp, f' ', không cần mở ngoặc đơn

# Định dạng bằng phương thức format
danhsach ="a:{}, b: {}, c: {}".format(1,2,3)
print(danhsach) #a:1, b: 2, c: 3
keyword = "Nếu muốn {} thì việc {} chớ để {}. Kẻ {} luôn tìm mọi lý do".format("thành công", "hôm nay", "ngày mai", "thất bại")
print(keyword)
# Định dạng output, tăng tính thẩm mỹ:
# Căn lề trái: {:(c)<n}
# Căn lề phải: {:(c)>n}
# Căn giữa:    {:(c)^n}
#Trong đó: c là kí tự điền vào chỗ trống
#n: là số kí tự dùng để căn, ví dụ c là *, n=3 => ***
row_1 = '+ {:*<10} + {:*^25} + {:*>10} +\n'.format('', '', '')
row_2 = '| {:<10} | {:^25} | {:>10} |\n'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<10} | {:^25} | {:>10} |\n'.format('0303', 'Sony', 'TP HCM')
row_4 = '| {:<10} | {:^25} | {:>10} |\n'.format('669', 'Kquiz', 'Da Lat')
row_5 = '+ {:-<10} + {:-^25} + {:->10} +\n'.format('', '', '')
print(row_1, row_2, row_3, row_4, row_5)
# cách gọn hơn
a = '| {:<6} | {:^20} | {:>20} |\n'
c1 = ' + {:-<6} + {:-^20} + {:->20} +\n'.format('','','')
c2 = a.format('id','họ và tên','nơi sinh')
c3 = a.format('132132123','Sony','TP.HCM')
c4 = a.format('1223123124','Thanh Teo','Ha Noi')
c5 = c1
print( c1,c2,c3,c4,c5)
# danh sách thành viên đã chích vaccine
p = "Pfizer"
ast = "Astra"
mor = "Morderna"
sin = "Sinopharm"
a1 = "{:^10} ~ {:^30} ~ {:<20} ~ {:^20}\n "
a2 = a1.format("ID", "Họ và Tên", "SĐT", "Loại Vaccine")
a3 = a1.format("025934690","Nguyễn Sony","0902624475", ast)
a4 = a1.format("123456788","Nam Quốc","0937072319", mor)
a5 = a1.format("093213123","Thị Hè","0903217872", sin)
a6 = a1.format("0128777827","Nam Văn Trọng","0903217874",p)
print(a2,a3,a4,a5,a6) 
