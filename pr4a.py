A=[] 
totals=int(input("Enter total no. of Students : "))

for i in range(totals):
    n=int(input(f"Enter the roll no of students {i + 1} : "))
    A.append(n)

print(A)

key=int(input("Enter the Key to find out the Roll no. : "))

def linear(A,key):
  flag=0
  for i in range(0,len(A)):
    if A[i]==key:
      flag=A[i]
      
    if flag == 0:
        print("Key Not Found ")
        A.append(key)
    else:
        print("Key Found " )
    
linear(A,key)     