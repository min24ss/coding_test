#https://www.acmicpc.net/problem/15649
#n과 m

n, m = map(int, input().split())


def dfs(path):
    if len(path) == m:
        print(*path) # *: 언패킹 연산자, 리스트 안의 원소 풀어서 함수에 전달 
        return
    for i in range(1, n+1):
        if i not in path:
            dfs(path+[i])
dfs([])