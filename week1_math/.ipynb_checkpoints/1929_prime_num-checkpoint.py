#https://www.acmicpc.net/problem/1929
#M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# ex 3, 16
m, n = map(int, input().split())

for i in range(m, n+1):
    if i < 2: 
        continue
    for k in range(2, int(i ** 0.5)+ 1):
        if i % k ==0 :
            break
    else:
        print(i)