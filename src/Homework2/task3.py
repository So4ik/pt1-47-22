"""оздайте кортеж из одного элемента, чтобы при итерировании по этому элементу последовательно
выводились значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1."""
CORTAGE = ("123",)
# SPISOK = list(CORTAGE)
# print(SPISOK)
for i in CORTAGE:
    print(i)
    # , sep=" ", end="\n"
    # Пытался разделить объект внутри кортежа, чтобы на новой строке выводилось последовательность.
print(len(CORTAGE))