# Поиск дубликатов в списке
spisok = [1, 2, 3, 4, 5, 5]  # список для работы
newSpisok = []  # список в который будем сортировать элементы без дубикатов
for item in spisok:  # перебираем элементы списка для работы
    if item not in newSpisok:  # Если элемента нет в новом списке, - добавить его
        newSpisok.append(item)
print(newSpisok)
