"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
"""
s = int(input("Введите сумму: "))
p = int(input("Введите произведение: "))

for x in range(1, 1001):
    y = s - x
    if x * y == p:
        print("Ответ: X =", x, ", Y =", y)
        break
else:
    print("Нет таких X и Y.")