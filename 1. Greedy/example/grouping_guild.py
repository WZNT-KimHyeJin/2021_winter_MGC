# 모험가 길드 공포도 그루핑
# 여행을 떠날 수 있는 그룹 수의 "최댓값".
# ==> 모든 모험가가 떠나지 않아도 됨

num = int(input("모험가 명수를 입력하시오 :"))
data = list(map(int, input("공포도를 입력하시오 : ").split()))
data.sort()

result =0 # 그루핑한 그룹의 총 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    count +=1
    if count>= i:
        result +=1
        count =0

print("그룹 수 :",result)

# 내림차순으로 정렬해서 공포도가 큰 값부터 묶어야 하는 줄 알았는데 그게 아니었다..ㅠ
