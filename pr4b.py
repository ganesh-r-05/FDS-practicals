def accept(n):
    
    print('Enter Rollno of students attended training program : ')
    for i in range(0,n):
        roll = int(input())
        A.append(roll)

def Display():
    for i in range(0,n):
        print(A[i],end=" ")

def Iterative():
    l = 0;
    h = (len(A)) - 1
    key = int(input('Enter the value you are searching for : '))

    while(l<=h):
        mid = (l+h)//2

        if(A[mid] == key):
            print('Element Found at ',mid+1)
            break
        else:
            if(A[mid]>key):
                h = mid-1
            elif(A[mid]<key):
                l = mid+1
        
    print('Element Not Found !!')
        

def Recursive(l,h,key):
    

    if(l<=h):
        mid = (l+h)//2

        if(A[mid]==key):
            return mid
        
        else:
            if(A[mid]<key):
                l = mid +1
                Recursive(l,h,key)
            else:
                h = mid -1
                Recursive(l,h,key)
    
    else:
        return 0

def Fibonacci():
    key = int(input('Enter the elements you want to search : '))


# def Fibonacci():

while(True):
        print('1. Accept and Display List')
        print('2. Recursive Binary Search')
        print('3. Iterative Binary Search')
        print('4. Fibonacci Search')
        print('5. Quit')
        print()
        ch = int(input('Enter Your Choice : '))

        A = []
        if(ch==1):
            
            n = int(input('Enter Total number of students attending program :  '))
            accept(n)
            Display()
            print()

        elif(ch==2):
            l = 0;
            h = l + (len(A) - 1)
            key = int(input('Enter the value you are searching for : '))
            el = Recursive(l,h,key)
            if(el==0):
                print('Element Not Found !!')
            else:
                print('Element Found at : ',el)

        elif(ch==3):
            Iterative()
        elif(ch==4):
            Fibonacci()
        elif(ch==5):
            quit()
        else:
            print('Invalid Choice !!')