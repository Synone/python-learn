M=[[1,2,3]
,[4,5,6],
[7,8,9]] # đây gọi là ma trận 2 chiều
print(M[1][2])
# lấy chéo 
diag = [M[i][i] for i in [2,0,1]] 
print(diag)

# List Comprehension
col2 = [row[1] for row in M] #collect the items in column 2
print(col2) # [2,5,8]
#“Give me row[1] for each row in matrix M, in a new list.” #
# The result is a new list containing
# column 2 of the matrix.

col3 = [row[1] + 1 for row in M]
print(col3)


number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])

for row in number_grid:
    for col in row:
        print(col)







