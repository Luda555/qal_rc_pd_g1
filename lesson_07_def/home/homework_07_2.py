# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    result = number * multiplier
    while True:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

  

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел."""
def sum_2_numbers(num1, num2):
    return num1 + num2

print(sum_2_numbers(11, 17))

add_numbers = lambda x, y: x+y
print(add_numbers(15, 7))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean(numbers_list):
#виводить середнє арифметичне
    return sum(numbers_list) / len(numbers_list)
print(arithmetic_mean([3,8,9,5]))






# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_str(text):
    #виводить заданий текст у зворотньому порядку
    return text[::-1]
print(reverse_str("Реве та стогне Дніпр широкий"))  

def reverse_str2(text):
    #виводимо текст у зворотньому порядку через reversed + .join
    return "".join(reversed(text))
print(reverse_str2("Широкий вітер завива"))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def max_word(list_words):
    return max(list_words)
print(max_word(["День", "велосипед", "собака", "сон"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""# Вправа 7: Зворотний порядок цифр
print("\n=== ВПРАВА 7: Зворотний порядок ===")
print("Виведіть цифри числа у зворотному порядку")

def reverse_number(*numbers):
    return numbers[::-1]
print(reverse_number(2, 7, 8, 9))

def reverse_number(number):
    new_number = str(number)[::-1]
    return int(new_number)
print(reverse_number(3465))


# Вправа 8: Пошук максимального числа
print("\n=== ВПРАВА 8: Пошук максимального ===")
print("Знайдіть найбільше число серед введених")
print("Введіть 0 для завершення")

def max_number(*number):
    return max(number)
print(max_number(21, -5, 77, 0, 17))

# Вправа 9: Виключення зі списку
print("\n=== ВПРАВА 9: Виключення зі списку ===")
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]

def fruits(list_fruits):
    # delete orange
    return[fruit for fruit in list_fruits if fruit != "orange"]
print(fruits(["apple", "banana", "orange", "grape", "mango"]))


fruits_list = ["apple", "banana", "orange", "grape", "mango"] 
fruits_list.pop(2)
print(fruits_list)

def fruits_list_1(fruits1):
    fruits1.remove("orange")  
    return fruits1  
my_fruits = ["apple", "banana", "orange", "grape", "mango"] 
print(fruits_list_1(my_fruits))

# Вправа 10: Вираз в один рядок
print("\n=== ВПРАВА 10: Вираз з умовою в один рядок ===")
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = ["Відповідь вставте сюди"]
print(result)  #  [4, 16, 36, 64, 100]

def square_of_numbers(list_numbers):
    #виводимо степінь парних чисел зі списку
    return[number**2 for number in list_numbers if number % 2 == 0]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(square_of_numbers(numbers))