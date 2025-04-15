# num1 = int(input("Введите число диапазона 1 : "))
# num2 = int(input("Введите число диапазона 2 : "))
# x = 0
# if num1>num2: num1,num2 = num2,num1
# while num1 <= num2:
#     if num1 % 4 == 0:
#         print("Числа кратные 4,",num1)
#         num1 += 4
#     else:
#         num1 += 1
# for i in range (2,10,2):
#     print(i,end=" ")
import random

# num1 = int(input("Введите число диапазона 1 : "))
# num2 = int(input("Введите число диапазона 2 : "))
# if num1>num2: num1,num2 = num2,num1
# x = 0
# for i in range(num1, num2):
# a = int(input("Введите число: "))
# sum = 0
# while a:
#       sum+=a%10
#       a = a//10
# print(sum)
# #
# a = int(input("num: "))
# for i in range(1,11):
#       print(a,"*",i, "=",a*i)
import random
a = random.randint(10,99)
print("Загаданное число",a)
flag = True
yes = True
count = 0
while yes and flag and count < 5:
      count+=1
      b = int(input("Введите число: "))
      if b > a:
            print("Ваше число больше загаданного ")
      elif b < a:
            print("Ваше число меньше загаданного ")
      else:
            print("Ура")
            flag=False
      if count==5:
            print("Вы проиграли. Сыграть снова? Yes, No ")
            vibor = input(" ")
            if vibor != "Yes":
                  break
print("Вы сделали",count," попыток")










