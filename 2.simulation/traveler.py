n = int(input("크기를 입력하시오: "))

input_lst = input("요구사항을 입력하시오 : ").split()

# 공간에서 상황이 이루어진다고 해도 굳이 2차원 배열을 만들지 않고 진행할 수 있다.
x = 1;
y =1;

for i in input_lst:
    if i == 'R': x+=1
    elif i == 'L': x-=1
    elif i == 'U': y-=1
    elif i == 'D': y+=1
    else: print("올바르지 않은 입력입니다.")

    if x == 0 : x=1
    elif x>n : x=n

    if y == 0: y = 1
    elif y > n: y = n


print("여행자의 좌표는 : (",y,',',x,')입니다')

# 첫째 줄에 공간의 크기를 나타내는 N이 주어진다(1<=N<=100)
# 둘때 줄에 여행가 A가 이동할 계획서 내용이 주어진다.

# 여행가 A가 최종적으로 도착할 지점의 조표 (X,Y)를 공백을 기준으로 구분하여 출력한다.


