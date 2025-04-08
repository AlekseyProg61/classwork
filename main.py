# a = int(input('ведите число 1 : '))
# b = int(input('ведите число 2 : '))
# if a>b:a,b=b,a
# while a<=b:
#         print((a+b)/2)
#         a+=1

# n = int(input("Введите количество повторений:  "))
# x = 0
# while n > 0:
#         a = int(input("Введите число: "))
#         if a == 3:
#                 n-=1
#                 print(a)
#                 x += 1
#         else:
#                 print(x)

# n = int(input("Введите количество чисел:  "))
# x = 0
#
# while n > 0:
#         a = int(input("Введите число: "))
#         print(a+a)
#         n-=1


# n = int(input("Введите количество чисел:  "))
# x = 0
#
# while n > 0:
#         a = int(input("Введите число: "))
#         if x >= a:
#                 x = a
#                 print(x)
#         n-=1
# else:
#         print(a)

n = int(input("Число: "))
x = 0
while n != x:
        if n >= x:
           print("*",end="")
        n-=1
