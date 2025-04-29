from random import randint
a = int(input("Введите число диапазона 1 : "))
b = int(input("Введите число диапазона 2 : "))
d = 1
f = 1
if a > b:
    a, b = b, a
while f <= b:
    c = randint(1, 100)
    print(c)
    if c == d:
        print("Компьютер угадал число в вашем диапазоне",d,"=",c)
    elif c != d:
        print("Попытка компьютера",d)
    elif d > c:
        print("Вы ввели диапазон больше 100")
    d += a
    f += 1
print(f"Компьютер сделал {d} попыток")