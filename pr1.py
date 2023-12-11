A=[]
total=int(input("Enter the total no. of students :"))
def userinput():
  for i in range(total):
    mark=int(input(f"Enter the marks of students {i+1}:"))
    A.append(mark)

def average():
  add = 0
  for i in range(0,mark):
    add = add + A[i]
    avg = add / mark
    print("Average of Student Marks :", avg)

def lowest():
  low=A[0]
  for i in range(0,mark-1):
    if(A[i+1]<low):
      low=list[i+1]
      print("Lowest Marks is :",low)


def highest():
  high=A[0]
  for i in range(0,mark-1):
    if(A[i+1]>high):
      high=list[i+1]
      print("Highest Marks is :",high)

def absentcount(A):
  abs = sum(1 for mark in A if mark<0)
  print("Absent Student :",abs)

def maxfrequency():
  maxfreqn = highest()
  for i in range(0,mark):
    if maxfreqn==A[i]:
      count = count + 1
      print("Max Frequency is : ", count)


userinput()
average()
lowest()
highest()
absentcount(A)
maxfrequency()