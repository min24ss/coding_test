#https://www.acmicpc.net/problem/8393
#n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
#ex. 3일 때 결과 6 

n = int(input())

answer = 0 

for i in range(n+1):
    answer += i
    print(answer)