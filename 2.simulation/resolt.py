data = input("문자열을 입력하시오 :")
result = []
value =0

for x in data:
    if x.isalpha():
        result.append(x)

    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))
print(''.join(result))