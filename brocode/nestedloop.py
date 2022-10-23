rows = int(input("How many rows?: "))
columns = int(input("How many co:: "))
symbol = input ("Enter a sybol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end = " ")
    print()