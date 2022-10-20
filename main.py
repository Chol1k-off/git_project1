chislo1 = 0
chislo2 = 1
vvod = int(input("Введите номер последнего элемента числа Фибаначчи: "))
for i in range(vvod):
    sum= chislo1 + chislo2
    chislo1 = chislo2
    chislo2 = sum
print("Ответ =",chislo1)