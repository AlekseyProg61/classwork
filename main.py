# numbers = [15,18,23,20,13,11,8,19,17,1,6]
# a = int(input("Введите число: "))
# b = 0
# for i in range(a):
#     print(numbers[random.randint(0, len(numbers)-1)],end="")
numbers = [-6, -15, -14, 15, 18, 23, 20, 13, 11, 8, 19, 17, 1, 6, 28]
b = 0
summ_negative = 0
summ_odd = 0
summ_even = 0
sum_sum = 0
work = 1
min = numbers[0]
max = numbers[0]
min_index = 0
max_index = 0
mult = 1
# for i in numbers:
#     if i % 2 == 0:
#         summ_negative += i
#         print(i)
#     else:
#         summ_even += i
#         print(i)
#     if i < 0: summ_negative += i
#     print(i)
# for i in range(0,len(numbers),3):
#     i*=work
#     print(i)
# for i in range(0, len(numbers)):
#     if min < numbers[i]:
#         min = numbers[i]
#         min_index = i
#         print(numbers[i])
#     if max < numbers[i]:
#         max = numbers[i]
#         max_index = i
#     for j in range(min_index, max_index):
#         mult *= numbers[j]
#         print("Произведение ", mult)

# for i in range(0, len(numbers) - 1):
#     if min > numbers[i]:
#         min = numbers[i]
#         min_index = i
#     if max < numbers[i]:
#         max = numbers[i]
#         max_index = i
#
# if min_index > max_index: min_index, max_index = max_index, min_index
first_index = 0
last_index = 0
for i in range(0,len(numbers)-1):
    if first_index > 0:
        first_index = numbers[i]
        break
    for j in range(len(numbers),0,-1,):
        if last_index > 0:
            last_index = numbers[j]
        if first_index>last_index: last_index,first_index = first_index,last_index
        for q in range(first_index,last_index):
            first_index+=q
            print(q)
