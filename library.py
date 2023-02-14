
import os


library = [
    {
        "название": "Введение в Python. Том 1",
        "автор": "Марк Лутц",
        "год": 2022
    },
    {
        "название": "Введение в Python. Том 2",
        "автор": "Марк Лутц",
        "год": 2022
    },
    {
        
        "название": "Искусство программирования",
        "автор": "Дональд Кнут",
        "год": 2019
    },
    {
        "название": "Грокаем алгоритмы",
        "автор": "Бхаргава Адитья",
        "год": 2020    
    }
]


def show_books() -> None:
    """ выводит на экран все книги библиотеки, пронумеровав их с 1 """
    os.system("cls")
    if not library:
        print("Библиотека пуста")
        return
    for num, book in enumerate(library, 1):
        print(f"номер на полке: {num}")
        print(f"название: {book['название']}")
        print(f"автор: {book['автор']}")
        print(f"год: {book['год']}")
        print("")
    return


def add_book() -> None:
    """ добавляет книгу в библиотеку, в книге обязательно заполненыф 3 поля """
    os.system("cls")
    title = input("Введите название книги: ")
    if not title:
        print("Ошибка! Нет названия.")
        return

    author = input("Введите имя автора книги: ")
    if not author:
        print("Ошибка! Нет автора.")
        return

    year = input("Введите год издания книги: ")
    if year.isdigit():
        year = int(year)
    else:
        print("Ошибка! Год должен быть целым числом.")
        return

    book = {
        "название": title,
        "автор": author,
        "год": year
    }

    if book in library:
        print("Ошибка! Такая книга уже есть.")
        return

    library.append(book)
    print("Книга успешно добавлена в библиотеку!")
    return

def remove_book() -> None:
    """ удаляет книгу из библиотеки по порядковму номеру ( >0 ) """
    os.system("cls")
    num = input("Введите номер книги для удаления: ")
    
    if not num.isdigit():
        print("Номер должен быть целым числом")
        return
    else:
       num = int(num)

    idx = num -1 

    if idx < 0:
        print("Номер должен быть целым положительным числом")
        return

    if idx > len(library) - 1:
        print("Нет такой книги")
        return

    print(f"Книга {library[idx]} удалена")
    library.pop(idx)
    return 


    
def find_book_by_number() -> None:
    """ Ищет книгу по порядковому номеру и показывает ее """
    os.system("cls")
    num = input("Введите порядковый номер книги: ")

    if not num.isdigit():
        print("Номер должен быть целым положительным числом")
        return
    else:
       num = int(num) 

    idx = num - 1

    if idx < 0:
        print("Номер должен быть целым положительным числом")
        return

    if idx > len(library) - 1:
        print("В библиотеке нет такой книги")
        return

    book = library[idx]

    print("Книга найдена!")
    print(f"номер на полке: {idx + 1}")
    print(f"название: {book['название']}")
    print(f"автор: {book['автор']}")
    print(f"год: {book['год']}")
    return


def search_book_by_key(user_key: str) -> None:
    """Показывает книгу по ключу, если он есть """
    os.system("cls")
    
    if not library:
        print("В библиотеке нет книг")
        return 

    user_value = input(f"Введите {user_key}: ")  

    if not user_value:
        print("Ошибка! Пусто!")
        return


    if user_key == "год" and user_value.isdigit():
        user_value = int(user_value) 


    books_found = 0
    for book in library:
        if book[user_key] == user_value:
            books_found += 1
            print(f"номер на полке: {library.index(book) + 1}")
            print(f"название: {book['название']}")
            print(f"автор: {book['автор']}")
            print(f"год: {book['год']}")


    if not books_found:
        print("Книг не найдено, возможно вы ввели не верные смоволы, пожалуйста препроверьте")
    return



def visit_library() -> None:
    while True:
        print("Приветствуем вас в библиотеке, что вы хотите сделать")
        
        options = [
            "Показать книгу",
            "Добавить книгу",
            "Удалить книгу",
            "Показать книгу по порядковому номеру",
            "Найти книгу по названию",
            "Найти книгу по автору",
            "Найти книгу по году",
            "Выйти из програмы",
        ]

        for num, option in enumerate(options):
            print(f"{num}. {option}")

        key_library = input("Введите номер и нажмите ENTER")
        if key_library == "0":
            show_books()    
        elif key_library == "1":
            add_book()    
        elif key_library == "2":
            remove_book()    
        elif key_library == "3":
            find_book_by_number()
        elif key_library == "4":
            search_book_by_key('название')
        elif key_library == "5":
            search_book_by_key('автор')
        elif key_library == "6":
            search_book_by_key('год')
        elif key_library == "7":
            break
        else:
            ("Неверная опция, попробуйте ввести другую!")



# тестирование
visit_library()
