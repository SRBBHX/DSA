n = int(input("Enter length of array: "))
arr = []
print("Enter values")
for i in range(n):
    arr.append(int(input()))
maxSum = 0
currSum = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        currSum = 0
        for k in range(i, j + 1):
            currSum += arr[k]
        maxSum = max(maxSum, currSum)
print("Max Sum:", maxSum)
