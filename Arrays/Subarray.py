n = int(input("Enter the length of array: "))
arr = []
print("Enter Array:")
for i in range(n):
    arr.append(int(input()))
for i in range(len(arr)):
    for j in range(i, len(arr)):
        print("(", end="")
        for k in range(i, j + 1):
            print(arr[k], ", ", end="")
        print(")")
