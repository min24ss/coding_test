# #9020 골드바흐의 추측
# #https://www.acmicpc.net/problem/9020
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.

# 출력
# 각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.

#단계별 생각

#단계별 생각
#1. 처음에 입력 int()개 받고 (t)
#2. 입력 받은 수 만큼 입력받기
#3. 입력 받은 수의 소수 저장
#4. 저장된 소수 중 두 소수의 차이가 가장 적은 것 출력

t = int(input())
li = []

for i in range(1, t + 1):
    li.append(int(input()))

def is_prime(x):
    if x < 2:
        return False
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            return False
    return True

for n in li:
    for a in range(n // 2, 1, -1):  
        b = n - a
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
