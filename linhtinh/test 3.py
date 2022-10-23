 
def sum_num(i):
  previous_num = 0
  for num in range(0,i+1): # chu y thu tu execute cua vong lap 
    sum =  previous_num + num
    print("Current number: ", num, " Previous number: ", previous_num, " Sum: ", sum)
    previous_num = num
sum_num(10)
#-------------------------------------------------
a = "pynative"
print(a.find("p"))
#=------------------------------------------------
def find_string(string):
  for word in string:
    if string.find(word)%2 !=0:
      continue
    else:
      print(word, end =" ")
  print()
##--------------------------------------
def remov_char(a,b):
  a = a[b:]
  print(a)
remov_char("pynative",4)
#--------------------------------------------
def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x
#=====================================
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
def t_or_f(list):
  l = len(list) -1
  if list[0] == list[l]:
    return True
  else:
    return False
a = t_or_f(numbers_x)
print(a)
print(t_or_f(numbers_y))

######### --------------
given_list = [10,20,33,46,55]
for num in given_list:
  if num%5!=0:
    continue
  else:
    print(num)
 
#### 
n =1
for num in range(6):
  for i in range(num):
    print(num,end="")
  print("\n")




