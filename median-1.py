# median of two sorted arrays of same sizes

arr = []
arr1 = [10, 13, 17, 30, 45]
arr2 = [1, 2, 3, 4, 5]

i = 0
j = 0
n = len(arr1) + 1
for k in range(n):
    if(i == len(arr1)):
        arr.append(arr2[j])
        break
    elif(j == len(arr1)):
        arr.append(arr1[i])
        break
    if(arr1[i] < arr2[j]):
        arr.append(arr1[i])
        i += 1
    else:
        arr.append(arr2[j])
        j += 1
print(arr)
median = (arr[-1] + arr[-2]) / 2
print(median)