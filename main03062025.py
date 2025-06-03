# import random
#
# list = []
# for i in range(1000):
#     list.append(random.randint(100,999))
# list2 = list.copy()
# print(list)
# print(list2)
# def bubble_sort(list):
#     count = 0
#     for i in range(len(list)):
#         flag = False
#
#         for j in range(len(list)-1 - i):
#             count += 1
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
#         flag = True
#         if not flag:
#             break
#     print(count)
#
# if __name__ == "__main__":
#     bubble_sort(list)
#     print(list)

list = [3, 7, 1, 5, 4, 6, 8]


# def insertion_sort(list):
#     count = 0
#     for i in range(1,len(list)):
#         for j in range(i,0,-1):
#             count += 1
#             if list[j] < list[j-1]:
#                 list[j],list[j-1] = list[j-1],list[j]
#             else:
#                 break
#
#
#     print(count)
#
# if __name__ == "__main__":
#     insertion_sort(list)
#     print(list)


# def cockteil_sort(list):
#     print("Несортированный список =", list)
#     length = len(list)
#     start_index = 0
#     end_index = length - 1
#     flag = True
#     count = 0
#     while (start_index < end_index):
#         for i in range(start_index, end_index):
#             if list[i] > list[i + 1]:
#                 list[i], list[i + 1] = list[i + 1], list[i]
#                 flag = False
#                 if flag:
#                     break
#                 print(list)
#             end_index = end_index - 1
#             flag = True
#             for j in range(end_index, start_index, -1):
#                 if list[j] < list[j - 1]:
#                     list[j], list[j - 1] = list[j - 1], list[j]
#                     flag = False
#                     if flag:
#                         break
#                     print(list)
#                 start_index = start_index + 1
#
#
# if __name__ == "__main__":
#     cockteil_sort(list)
#     print("Сортированный список", list)
list = [2,2,5,3,6,2,5,7,3,7,9,8,7,9,1,4,0]

def max_list(list):
    max_l = 0
    for i in range(len(list)):
        if i > max_l:
            max_l = i
            return max_l
def counting_sort(list):
    max = max_list(list)
    list = [0 for i in range(max+1)]
    print(list)
    for i in list:
        list[i]+=1
    for i in range(len(list)):
        while (list[i]>0):
            result_list = list.append(i)
            list[i]-=1
    return result_list

if __name__ == "__main__":
    counting_sort(list)
    print("Сортированный список",list)