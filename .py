# Функция 1
def insert_middle(lst, string):
    # Определяем индекс середины списка
    middle_index = len(lst) // 2
    
    # Если длина списка нечетная, вставляем строку перед серединным элементом
    if len(lst) % 2 != 0:
        lst.insert(middle_index, string)
    else:
        # Если длина списка четная, вставляем строку после серединного элемента
        lst.insert(middle_index, string)
    
    return lst

# Пример использования функции 1
lst1 = ['a', 'b', 'c']
string1 = 'x'
result1 = insert_middle(lst1, string1)
print("Результат функции 1:", result1)  # Результат: ['a', 'x', 'b', 'c']

# Функция 2
def insert_at_position(lst, pos, string):
    # Если указанная позиция больше длины списка или меньше 0
    if pos < 0 or pos > len(lst):
        return "operation is not possible"
    lst.insert(pos, string)
    return lst

# Пример использования функции 2
lst2 = ['a', 'b', 'c']
pos = 2
string2 = 'x'
result2 = insert_at_position(lst2, pos, string2)
print("Результат функции 2:", result2)  # Результат: ['a', 'b', 'x', 'c'] 
