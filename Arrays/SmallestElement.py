n = int(input("Enter length of array: "))
arr = []
print("Enter element")
for i in range(n):
    arr.append(int(input()))
smallest = arr[0]
for i in range(len(arr)):
    if smallest > arr[i]:
        smallest = arr[i]
print("Smallest Element:", smallest)
