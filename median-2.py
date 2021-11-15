# median of two sorted arrays of different sizes

arr = []
arr1 = [-5, 3, 6, 12, 15]
arr2 = [-12, -10, -6, -3, 4, 10]

N = len(arr1) + len(arr2)

i = 0
j = 0
n = max(len(arr1) + 1, len(arr2) + 1)
for k in range(n):
    if(i == len(arr1)):
        arr.append(arr2[j])
        j += 1
        continue
    elif(j == len(arr2)):
        arr.append(arr1[i])
        i += 1
        continue
    if(arr1[i] < arr2[j]):
        arr.append(arr1[i])
        i += 1
    else:
        arr.append(arr2[j])
        j += 1

print(arr)

if(N % 2 == 0):
    m1 = int(N / 2)
    m2 = int(m1 - 1)
    median = (arr[m1] + arr[m2]) / 2
else:
    m1 = int(N // 2)
    median = arr[m1]
print(median)