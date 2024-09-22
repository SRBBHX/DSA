n = int(input("Enter length of array: "))
arr = []
print("Enter element")
for i in range(n):
    arr.append(int(input()))
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        print("(", arr[i], ",", arr[j], ")", end="")
