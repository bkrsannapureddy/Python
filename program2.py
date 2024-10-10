def divisible(arr):
    for i in range(len(arr)):
       if arr[i]%5==0:
          print(arr[i])
arr=list(map(int,input().split()))
divisible(arr)
    