"""
1. Дано ціле число. Якщо воно є додатним, то відняти від нього 8; в іншому разі не змінювати його.
Вивести отримане числ
"""


def main(num):
    if num > 0:
        num -= 8
        return num
    else:
        return num

result = main(int(input('num = ')))
print(result)
input()