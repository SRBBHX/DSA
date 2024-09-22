n = int(input("Enter the length of array"))
arr = []
print("Enter values:")
for i in range(n):
    arr.append(int(input()))
maxSum = 0
currSum = 0
for i in range(len(arr)):
    currSum += arr[i]
    if currSum < 1:
        currSum = 0
    maxSum = max(currSum, maxSum)
print("Max Sum: ", maxSum)
