C = []
cricket = int(input("Enter total no. of students who play cricket :"))
for i in range(cricket):
  croll = int(input(f"Enter the roll no. of students who play cricket {i+1}:"))
  C.append(croll)
B = []
badminton = int(input("Enter total no. of student who play Badminton :"))
for i in range(badminton):
  broll = int(
      input(f"Enter the roll no. of students who play badminton {i+1} :"))
  B.append(broll)
F = []
football = int(input("Enter the no. of student who play Football :"))
for i in range(football):
  froll = int(input("Enter the roll no. of student who play football :"))
  F.append(froll)

U = []
U.extend(C)
U.extend(B)
U.extend(F)

u = len(U)
print("Universal Set of All sports :", U)
print("Students who play Cricket : ", C)
print("Students who play Badminton : ", B)
print("Students who play Football : ", F)

#Que1
CD = []
for i in range(cricket):
  if C[i] in B:
    CD.append(C[i])
print("Students who play Cricket & Badminton Both : ", CD)

#Que2
E = []
for i in range(cricket):
  if C[i] not in CD:
    E.append(C[i])

for i in range(badminton):
  if B[i] not in CD:
    E.append(B[i])

print("Students who play either Cricket or Badminton but not both : ", E)

#Que3
AUB = []
FB = []
for i in range(u):
  if U[i] not in AUB:
    FB.append(U[i])
print("Students who play neither Cricket nor Badminton :", FB)
fb = len(FB)
print("No. of students who play neither Cricket nor Badminton :", fb)

#Que4
AUC = []
G = []
auc = len(AUC)
for i in range(auc):
  if AUC[i] not in B:
    G.append(AUC[i])
print("Students who play Cricket & football but not Badminton", G)
g = len(G)
print("No. of students who play Cricket & football but not Badminton : ", g)
