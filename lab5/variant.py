a=input('Введите текст:')
a=a.split()
for i in a:
    i=i.strip(".,!?;:").lower()
    if i[0]==i[-1]:
        print(i)
