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

# num1 = int(input("Введите число диапазона 1 : "))
# num2 = int(input("Введите число диапазона 2 : "))
# if num1>num2: num1,num2 = num2,num1
# x = 0
# for i in range(num1, num2):
a = int(input("Введите число: "))
sum = 0
while a:
      sum+=a%10
      a = a//10
print(sum)

