n = int(input("Enter length of array"))
arr = []
for i in range(n):
    arr.append(int(input()))
largest = arr[0]
for i in range(len(arr)):
    if largest < arr[i]:
        largest = arr[i]
print(largest)
