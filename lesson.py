# --- Создание ---

empty = set()           # пустое множество
not_a_set = {}          # а это пустой словарь!
print(type(empty), type(not_a_set))

fruits = {"яблоко", "банан", "груша"}
print(fruits)


# --- Нет повторов ---

numbers = {1, 2, 2, 3, 3, 3}
print(numbers)          # {1, 2, 3}

names = ["Анна", "Олег", "Анна", "Вера", "Олег"]
unique_names = set(names)
print(unique_names)


# --- Добавление ---

fruits.add("киви")
fruits.add("яблоко")    # уже есть, ничего не изменится
print(fruits)


# --- Удаление ---

fruits.remove("банан")
print(fruits)

fruits.discard("манго")     # элемента нет, но ошибки не будет
# fruits.remove("манго")    # KeyError
print(fruits)


# --- Задача ---

# print(fruits[0])    # TypeError: у множества нет индексов

# Придумай, как получить из множества fruits один элемент

fruits_list = list(fruits)
print(type(fruits_list), fruits_list)


products = {"яблуко", "картопля"}
products = set()


products.remove("яблуко")
products.discard("картопля")