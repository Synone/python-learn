import os


'''import shutil
path = "D:\SQL\\sql.txt"
if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That's a directory!")
else:
    print("That location doesn't exist!")


text = "Have a nocie day \n this is some text \n have a good one \n"
try:
    with open("RSA.txt","w") as file: # use with open, the file will be closed automatically
        file.write(text)
except FileNotFoundError:
    print("THat file was not found")

# copyfile() = copies contens of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)
shutil.copyfile("RSA.txt","D:\\SQL\\copy.txt" )#src.dst'''

# MOVING file
import shutil

source = "test.txt"
if os.path.exists(source):
    print("That location exists!")
destionation = "C:\\Users\\BI 1998\\Desktop\\tesst.txt"
if os.path.exists(destionation):
    print("That's location exist.")
try: 
    if os.path.exists(destionation):
        print("there is already a file there")
    else:
        shutil.move(source,destionation)
        print(source +" was moved.")
except FileNotFoundError:
    print(source +" was not found")

### DELETE FILE
path ="C:\\Users\\BI 1998\\Desktop\\cmd.txt"
#os.remove("C:\\Users\\BI 1998\\Desktop\\tesst.txt")
#os.remove(path)
# os.rmdir(path) # delete directory




