# 배낭에 담을 수 있는 무게에 최대값은 15kg
# 담고자 하는 짐에 가치와 무게가 있다.
# 가치의 합이 최대가 되도록 짐을 고르는 방법

# 분할 가능 조합 문제 == 그리디 == 단가 계산
# 분할 불가 조합 문제 == DP or 백트래킹

cargo = [(4,12),(2,1),(10,4),(1,1),(2,2)]

def fractional_knapsack(cargo):
    capacity =15
    pack =[] # 단가 계산 역순 정렬 저장
    for c in cargo:
        pack.append((c[0]/c[1], c[0],c[1]))
        # 1. 단가 저장. 2. 가치 3. 무게 ==> 자료형 3개 튜플 저장
    pack.sort(reverse=True) # 역순 정렬

    # 단가 순 그리디 연산
    total_value : float =0
    for p in pack:
        if capacity -p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]
        else:
            fraction = capacity / p[2]
            total_value += p[1] * fraction
            break
    return total_value

r =fractional_knapsack(cargo)
print(r)