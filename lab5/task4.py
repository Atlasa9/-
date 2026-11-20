# Дан массив A размера N. Вывести его элементы в следующем порядке: A1, AN , A2, AN−1, A3, AN−2

n = int(input("Введите размер массива N: "))
if n <= 0:
    print("N должно быть положительным.")
else:
    a = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()))
    
    if len(a) != n:
        print(f"Ошибка: введено {len(a)} чисел, а ожидалось {n}.")
    else:
        result = []
        left = 0
        right = n - 1
        
        while left <= right:
            result.append(a[left])
            left += 1
            
            if left <= right:
                result.append(a[right])
                right -= 1
        
        print("Результат:", *result)