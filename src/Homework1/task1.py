"""
Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена, а также
количество S товара.Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: 111 Общая цена 9 рублей 60 копеек.
"""

ruble = int(input('Введите кол-во рублей'))
cent = int(input("Введите кол-во копеек"))
value = int(input("Количество товара"))
print("Общая цена товара :", ruble * value, "рублей", cent * value, "копеек")
