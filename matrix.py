#Addtion, Subtraction, Multiply

rows1 = int(input("Enter the number of rows of the Matrix 1:"))
cols1 = int(input("Enter the number of columns of the Matrix 1:"))

rows2 = int(input("\nEnter the number of rows of the Matrix 2:"))
cols2 = int(input("Enter the number of columns of the Matrix 2:"))

matrix1 = []
matrix2 = []
for x in range(0, rows1):
	list_x = []
	matrix1.append(list_x)
	for y in range(0, cols1):
		list_x.append(int(input("Enter the element of row " + str(x+1) +" of Matrix 1:")))

for x in range(0, rows2):
	list_y = []
	matrix2.append(list_y)
	for y in range(0, cols2):
		list_y.append(int(input("Enter the element of row " + str(x+1) +" of Matrix 2:")))
		
print("M1:",matrix1)
print("M2:",matrix2)

#Matrix Addition
add_result = []
if (rows1 != rows2  or cols1 != cols2):
	print("Dimensionality error")
else:
	for x in range (0, rows1):
		sum = []
		add_result.append(sum)
		for y in range (0, cols1):
			sum.append(matrix1[x][y] + matrix2[x][y])
	print("Sum:", add_result)

#Matrix Subtraction
sub_result = []
if (rows1 != rows2  or cols1 != cols2):
	print("Dimensionality error")
else:
	for x in range (0, rows1):
		subtract = []
		sub_result.append(subtract)
		for y in range (0, cols1):
			subtract.append(matrix1[x][y] - matrix2[x][y])
	print("Subtraction:", sub_result)

#Matrix Multiplication
mult_result = []
temp = 0
if(cols1 != rows2):
	print("Matrices are not conformable")
else:
	for x in range (0, rows1):
		mult = []
		mult_result.append(mult)
		for y in range(0, cols2):
			for z in range(0, cols1):
				temp += matrix1[x][z] * matrix2[z][y]
			mult.append(temp)
			temp = 0
	print("Multiplication:", mult_result)

		


