"""
Дан список целых чисел. 
Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2
"""
mainSpisok = [1, 2, 3, 4, 5]
newSpisok = []
for item in mainSpisok:
    newItem = item * -2
    newSpisok.append(newItem)
print(newSpisok)

mainSpisok = [1, 2, 3, 4, 5]
newSpisok = []
for item in mainSpisok:
    while item > 0:  # проверка на элементы боольше 0 с помощию while
        newItem = item*-2
        newSpisok.append(newItem)
        break
print(newSpisok)
