a=input('Введите текст:')
b=''
for i in a:
    if i!=' ':
        b+=i.lower()
if a=="":
    print('Слов нет')
else:
    if b==b[::-1]:
        print('Палиндром')
    else:
        print('Не палиндром')
