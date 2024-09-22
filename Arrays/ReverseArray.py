n = int(input("Enter length of array: "))
arr = []
print("Enter array: ")
for i in range(n):
    arr.append((int(input())))
start = 0
end = len(arr) - 1
while start < end:
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start += 1
    end -= 1
print(arr)
