# 1. Создаем переменную my_dict и присваиваем ей словарь
my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
# 2. Выводим на экран словарь my_dict
print("Dict:", my_dict)
# 3. Выводим одно значение по существующему ключу
existing_value = my_dict.get('Masha')  # Получаем год рождения Маши
print("Existing value:", existing_value)
# Выводим одно значение по отсутствующему ключу без ошибки
not_existing_value = my_dict.get('NonExistentKey', None)  # Возвращаем None для отсутствующего ключа
print("Not existing value:", not_existing_value)
# 4. Добавляем ещё две произвольные пары в словарь my_dict
my_dict['Kamila'] = 1981
my_dict['Artem'] = 1915
# 5. Удаляем одну из пар по существующему ключу и выводим значение
deleted_value = my_dict.pop('Egor')  # Удаляем пару с ключом 'Egor'
print("Deleted value:", deleted_value)
# 6. Выводим на экран измененный словарь my_dict
print( my_dict)

#  множества
# 1. Создаем переменную my_set и присваиваем ей множество
my_set = {1, 'Яблоко', 42.314, 1, 'Яблоко'}
# 2. Выводим на экран множество my_set
print("Set:", my_set)
# 3. Добавляем 2 произвольных элемента в множество
my_set.add(13)
my_set.add((5, 6, 1.6))
# 4. Удаляем один любой элемент из множества
my_set.pop()
# 5. Выводим на экран измененное множество my_set
print("Modified set:", my_set)

