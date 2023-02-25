# spisok = [1, 2, 3, 4, 5, 5, 6, 6]
# newSpisok = []
# summa = 0
# for item in spisok:
#     if spisok.count(item) >= 2:
#         newSpisok.append(item)
# print(newSpisok)
spisok = set([1, 2, 3, 4, 5, 6, 6])
newSpisok = set([])
newSpisok.update(spisok)
print(newSpisok)
