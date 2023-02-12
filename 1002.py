import math

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())  #두 원의 거리
    distnace = math.sqrt((x1-x2)**2 + (y1-y2)**2)   #원의 방정식
    
    if distnace == 0 and r1==r2:    #두 원이 동심원이고 반지름이 같을 때
        print(-1)
    elif abs(r1-r2) ==distnace or r1+r2 ==distnace: #두 원의 내접, 외접
        print(1)
    elif abs(r1-r2) < distnace < (r1+r2):   #두 원이 서로 다른 두 점에서 만날 때
        print(2)
    else:   
        print(0)    #그 외