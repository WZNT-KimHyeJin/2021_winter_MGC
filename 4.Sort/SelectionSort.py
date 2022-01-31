array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[i] > array[j]:
            min_index = j
    array[i],array[min_index] = array[min_index],array[i] # 이게 되네...?

print("선택정렬 결과 : ", array)