# https://www.acmicpc.net/problem/1978
### 소수 찾기
# ex. 첫 줄 4 다음 줄 1 3 5 7

m = int(input())
li = list(map(int, input().split()))
num = []
for i in li:
    if i < 2:
        continue
    for k in range(2, int(i **0.5) + 1):
        if i % k == 0:
            break
    else:
        num.append(i)
print(len(num))