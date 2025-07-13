n = int(input("введите n: "))
m = int(input("введите m: "))

first_List = m * [int(i) for i in range(1, n + 1)]
second_List = [' ']
third_List = []
iter = 0
while second_List[-1] != 1:
    second_List.clear()
    for j in range(iter, m + iter):
        second_List.append(first_List[j])
        iter += 1 
    second_List_copy = second_List.copy()
    third_List.append(second_List_copy)
    iter -= 1
for k in range(len(third_List)):
    print(third_List[k][0], end='')
