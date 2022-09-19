# заменить все пробелы на "-"
# Способ первый
text = "there should be a normal text here"
text = text.replace(' ', '-')
print(text)
# Способ второй
s = input()
l = s.split()
s1 = '-'.join(l)
print(s1)