rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

m1 = []
m2 = []

# Take user input for each element in the matrix
for i in range(rows):
  row = []
  for j in range(columns):
    element = int(input(f"Enter element at position ({i+1} ,{j+1}): "))
    row.append(element)
  m1.append(row)

# Print the resulting matrix
print("Entered matrix:")
for row in m1:
  print(row)

for i in range(rows):
  row = []
  for j in range(columns):
    element = int(input(f"Enter element at position ({i+1} ,{j+1}): "))
    row.append(element)
  m2.append(row)

# Print the resulting matrix
print("Entered matrix:")
for row in m2:
  print(row)


def add():
  result_add = []
  for i in range(rows):
    result_row = []
    for j in range(columns):
      result_ele = m1[i][j] + m2[i][j]
      result_row.append(result_ele)
    result_add.append(result_row)

  print("**********Addition is : ")
  for row in result_add:
    print(row)


def sub():
  result_sub = []
  for i in range(rows):
    result_row = []
    for j in range(columns):
      result_ele = m1[i][j] - m2[i][j]
      result_row.append(result_ele)
    result_sub.append(result_row)

  print("**********Subtraction is : ")
  for row in result_sub:
    print(row)


def mul():
  result_mul = []
  for i in range(len(m1)):
    result_row = []
    for j in range(len(m2[0])):
      element = 0
      for k in range(len(m2)):
       element  += m1[i][k] * m2[k][j]
      result_row.append(element)
    result_mul.append(result_row)

  print("**********Multiplication is : ")
  for row in result_mul:
    print(row)


def transpose():
  result_trans = []
  for i in range(rows):
    temp = []
    for j in range(columns):
      temp.append(m1[j][i])
    result_trans.append(temp)

  print("**********Transpose is : ")
  for row in result_trans:
    print(row)


add()
sub()
mul()
transpose()
