# Taking input for matrix dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Creating an empty matrix
matrix1 = []

# Taking input for matrix elements
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input("Enter element of first matrix : "))
        row.append(element)
    matrix1.append(row)
    
print("\nFirst matrix : ")
for row in matrix1:
    print(row)
    
matrix2 = []

# Taking input for matrix elements
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input("Enter element of second matrix : "))
        row.append(element)
    matrix2.append(row)
    
print("\nSecond matrix : ")
for row in matrix2:
    print(row)
         
result =  [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
print("\nResult of matrix addition : \n")
for row in result:
    print(row)