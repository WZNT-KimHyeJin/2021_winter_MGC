# N에 대하여 빼기1 또는 나누기 K를 적용하여
# 가장 빨리 1로 만들 수 있는 횟수를 탐색

n,k = map(int, input().split())
# 정수형 입력값 두 개를 공백을 기준으로 구분하여 입력 받는다.
result = 0

while True:
    target = (n//k)*k
    # k로 나누어 떨어지는 N이하의 가장 큰 수를 탐색

    # if target==0:
    #     cnt=n
    result+=(n-target)
    #입력받은 N에서 구한 target을 제외하고 뺄셈 연산 적용
    n=target

    if n<k:
        break
    result +=1
    n//=k # 나누기 연산이 가능한 횟수
result += (n-1) # 나누어지는 몫 -1 이 연산 횟수

print("총",result,"회")
