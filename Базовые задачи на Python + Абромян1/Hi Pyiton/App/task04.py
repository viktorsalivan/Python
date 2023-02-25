# spisok1 = [1, 2, 3, 4, 5]
# spisok2 = [6, 7, 8, 9, 10]
# spisokNew = []
# for item in spisok1:
#     spisokNew.append(item)
# for item in spisok2:
#     spisokNew.append(item)
# print(spisokNew)


# a = [1, 2, 3, 4, 5, 6]
# b = [6, 7, 8, 9, 10]
# rezult = filter(lambda x: x in a and x in b, a)
# print(list(rezult))


spisok1 = [1, 2, 3, 4, 5, 6]
spisok2 = [6, 7, 8, 9, 10]
spisokNew = []
for item in spisok1:  # проходимся по первому списку
    if item in spisok2:  # Если элемент первого списка есть во втором
        spisokNew.append(item)  # Добавить в новый список
print(spisokNew)
