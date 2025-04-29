year = int(input("Введите год своего рождения: "))
if year <= 1925 and year <= 1944:
    print("Молчаливое поколение")
elif year >= 1944 and year <= 1967:
    print("Поколение бэби-бумеров")
elif year >= 1967 and year <= 1984:
    print("Поколение X ")
elif year >= 1984 and year <= 2000:
    print("Поколение Y. Миллениалы ")
elif year >= 2000 and year <= 2011:
    print("Поколение Z. Зуммеры ")
elif year > 2011:
    print("Поколение альфа")
else:
    print("Нет значения")