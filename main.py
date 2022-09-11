# заменить все пробелы на "-"
# Способ первый
text = "there should be a normal text here"
text = text.replace(' ', '-')
print(text)
# Способ второй
a = 'there should be a normal text here'
def astra(mstr):
    print(mstr)
    res = a.sub(r'\s+', '-', mstr)
    print(res.split())
if __name__ == '__sff__':
    mstr = input()
    astra(mstr)
print(b)
# Ввести 3 числа, найти среднее арифмитическое с точностью до 3
# Ввести Имя, Возраст и Город, сформировать приветственное сообщение путем формирования 3-мя способами
# Ввести 3 числа, сказать сколько из них положительных и сколько отрицательных