#https://www.acmicpc.net/problem/4948
#베트르 & 공준
# 자연수 n보다 크고 2n 보다 작거나 같은 소수는 적어도 하나는 존재한다

max = 2 * 123456
is_prime = [True] * (max + 1) # 처음에 모든 수를 소수라고 가정
    #max + 1 인 리스트 만들고 모든 값에 True 채우기
    
is_prime[0] = is_prime[1] = False # 0과 1 소수 아님 -> 미리 False 로 변경
# [False, False, True, True.... ]

for i in range(2, int(max**0.5) + 1):
    if is_prime[i]: #i 가 소수이면
        for j in range(i*i, max+1, i): #i 배수 제거
            is_prime[j] = False

while True:
    n= int(input())
    if n == 0:
        break
    count = 0
    for i in range(n+1, 2*n + 1):
        if is_prime[i]:
            count += 1
    print(count)
    
            