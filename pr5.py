def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swapped = True
    if not swapped:
      break


total = int(input("Enter total students :"))
my_list = []
for i in range(0, total):
  d = int(input("Enter roll no. of students : "))
  my_list.append(d)

#selection sort
print("Selection sort ")


def selection_sort(arr):
  n = len(arr)
  for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
      if arr[j] > arr[min_index]:
        min_index = j


print("Original List : ")
print(my_list)

bubble_sort(my_list)
print("after Bubble Sort :")
print(my_list)

selection_sort(my_list)
print("After Selection sort :")
print(my_list)

top_five = my_list[5:]
print("Top Five Marks : ")
print(top_five)
