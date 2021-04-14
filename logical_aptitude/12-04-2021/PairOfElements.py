x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(x)):
    start_element = x[i]
    for j in range(i+1, len(x)):
        if start_element + x[j] == 100:
            print(f'pair of elements:{start_element},{x[j]}')
