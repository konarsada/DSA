N = 3
W = 50
values = [60,100,120]
weights = [10,20,30]

arr = []
P = 0

for i in range(len(values)):
    arr.append([values[i], weights[i]])

arr.sort(key=lambda x: x[0]/x[1], reverse=True)

for i in range(len(arr)):
    if(W > 0 and arr[i][1] <= W):
        W -= arr[i][1]
        P += arr[i][0]
    else:
        break

if(W > 0):
    P += arr[i][0] * (W / arr[i][1])

print(P)