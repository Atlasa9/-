# Работа с очередью

from collections import deque

queue = deque()

# 1–2. Создание и добавление
n = int(input("Сколько элементов добавить в очередь? "))
for i in range(n):
    val = input(f"Введите элемент {i+1}: ")
    queue.append(val)
print("Очередь после добавления:", *queue, "\n")

# 3. Получение элемента
if queue:
    item = queue.popleft()
    print(f"3. Извлечён первый элемент: {item}")
    print("Очередь теперь:", *queue, "\n")
else:
    print("3. Очередь пуста, извлекать нечего.\n")

# 4. Просмотр без удаления
if queue:
    print(f"4. Первый элемент (без удаления): {queue[0]}\n")
else:
    print("4. Очередь пуста.\n")

# 5–6. Пустота и размер
print(f"5. Очередь пуста? {len(queue) == 0}")
print(f"6. Размер очереди: {len(queue)}\n")

# 7. Проверка наличия
search_val = input("Введите значение для проверки наличия в очереди: ")
print(f"7. Элемент '{search_val}' есть в очереди? {search_val in queue}\n")

# 8. Очистка
confirm = input("Очистить очередь? (да/нет): ")
if confirm.lower() == "да":
    queue.clear()
    print("8. Очередь очищена.")
else:
    print("8. Очистка пропущена.")