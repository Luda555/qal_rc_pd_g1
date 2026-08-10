# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
small_list1 = list(set(small_list))
print(small_list1)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
print(sum(small_list) / len(small_list))

# task 3. Перевірте, чи є в списку big_list дублікати
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
has_duplicates = len(big_list) != len(set(big_list))
print(has_duplicates)
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
max_key = max(add_dict, key=add_dict.get)
print(max_key)

# task 5. Створіть новий словник, в якому ключі та значення base_dict будуть
# замінені місцями ({'Ukraine':'contry'...})
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
reversed_base_dict = {v:k for k,v in base_dict.items() }
print(reversed_base_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
sum_dict = base_dict.copy()
sum_dict.update(add_dict)
sum_dict['size'] = str(base_dict['size']) + str(add_dict['size'])
print(sum_dict)

# task 7.
line = "Створіть список з всіх символів, які входять у заданий рядок"
line_list = list(line)
print(line_list)

# task 8. Обчисліть суму елементів двох змінних через sum()
value_1  = [1, 2, 3, 4, 5]
value_2 = (4, 6, 5, 10)
sum_value_1_and_value_2 = sum(value_1 + list(value_2))
print(sum_value_1_and_value_2)
