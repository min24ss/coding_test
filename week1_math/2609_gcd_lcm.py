#최대공약수와 최소공배수 구하기
#2609

#두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
#입력
#첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
#출력
#첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력

n, m = map(int, input().split())
li = []
li2 = []
for i in range(1, n+1):
    if n % i == 0:
        li.append(i)
        

for j in range(1, m+1):
    if m % j == 0:
        li2.append(j)
        
gcd = max(set(li) & set(li2))

lcm = m * n // gcd
print(lcm)
