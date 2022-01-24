# 0~9로만 이루어진 문자열이 주어지고, 왼쪽부터 오른쪽으로 하나씩
# 모든 숫자를 확인하여 숫자 사이에 곱/덧 연산자를 넣어
# 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 문제.
# 단 모든 연산은 왼쪽에서부터 순서대로 이루어 져야 함.

data = input()

result = int(data[0])
# 입력받은 첫번째 문자를 숫자로 변경하여 대입

for i in range(1, len(data)):
    # ★★★ 두 수 중에서 하나라도 0 또는 1인 경우 더하기 수행
    num =int(data[i])
    if num <= 1 or result<=1:
        result+=num
    else:
        result *= num