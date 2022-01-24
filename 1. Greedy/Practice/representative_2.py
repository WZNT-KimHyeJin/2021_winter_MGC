n = int(input("명수를 입력하시오"))
lst=[]
for i in range(n):
    score_a, score_b = map(int, input("두 성적을 입력하시오 : ").split())
    lst.append((score_a,score_b))
lst.sort(reverse=True)
print("중간 점검",lst)
largest=lst[0][1]
cnt=0
for x,y in lst:
    if y>largest:
        largest=y
        cnt+=1
print(cnt)

# 두 개의 다르 항목을 비교하여 하나라도 큰 것을 찾을 때:
# 하나를 기준으로 내림차순 정렬 후 다른 하나는 서로 비교하여 큰 값이 되면 하나라도 큰 것.