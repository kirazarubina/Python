total_sum = 0
# Бесконечный цикл
while True:
    # Ввод с клавиатуры целого числа
    # int() - преобразует строку в число
    # input() - ожидает ввода с клавиатуры строки
    num = int(input())
    if num == 0:
        # Завершение цикла
        break
    if num % 6 == 0 and num % 10 == 4:
        total_sum += num
print(total_sum)