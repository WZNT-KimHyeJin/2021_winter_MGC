n = int(input("명수를 입력하시오 : "))
lst=[]
for _ in range(n):
    score_a, score_b = map(int,input("두 점수를 입력하세요. :").split())
    lst.append((score_a,score_b))

lst.sort()
cnt =n
for i in range(n):
    for j in range(n):
        if lst[i][0]< lst[j][0] and lst[0][i]< lst[0][j]:
            cnt -=1
            break

print(cnt)

# 시간 복잡도 ㅠㅠ