#피보나치 함수
p = int(input())

arr_0 = [1,0,1]
arr_1 = [0,1,1]



def fibo(n) :
    if len(arr_0) <= n :
        for i in range(len(arr_0), n+1) :
            arr_0.append(arr_0[i-1]+arr_0[i-2])
            arr_1.append(arr_1[i-1]+arr_1[i-2])
    print(arr_0[n],arr_1[n])
    

for i in range(p) : 
    n = int(input())
    fibo(n)
    