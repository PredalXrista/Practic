class Book:
    def __init__(self, name, autor, year, pages, availability):
        self.name = name
        self.autor = autor
        self.year = year
        self.pages = pages
        self.availability = availability

    def display_info(self):
        print(f"Название: {self.name}")
        print(f"Автор: {self.autor}")
        print(f"Год выпуска: {self.year}")
        print(f"Количество страниц: {self.pages}")
        print(f"Доступность: {self.availability}")

class DigitalBook(Book):
    def __init__(self, name, autor, year, pages, availability, format):
        super().__init__(name, autor, year, pages, availability)
        self.format = format

    def display_info(self):
        super().display_info()
        print(f"Формат книги: {self.format}")

def main():
    books = []

    while True:
        print("\n1: Добавить книгу")
        print("2: Взять книгу")
        print("3: Показать информацию о книге")
        print("4: Показать список всех книг")
        choice = input("Выберите действие:")

        if choice == "1":
            name = input("Введите название: ")
            autor = input("Введите автора: ")
            year = input("Введите год издания: ") 
            try:
                year = int(year)
                pass
            except ValueError:
                print("Недопустимое значение")
            pages = input("Введите количество страниц: ")
            try:
                pages = int(pages)
                pass
            except ValueError:
                print("Недопустимое значение")
            availability = input("Достпуна ли книга?: ")
            format = input("Книга digital (да/нет?): ").lower() == "да"
            if format:
                book = DigitalBook(name, autor, year, pages, availability, format)
            else:
                book = Book(name, autor, year, pages, availability)
            books.append(book)
            print(f"Книга {name} добавлена")

        elif choice == "2":
            if availability == "доступна":
                print("Вы взяли книгу")
                availability = "недоступна"
            else:
                print("незя")
            
        elif choice == "3":
            if not books:
                print("Нет книг для отображения")
            for book in books:
                book.display_info()
                print('-'*30)
                  
        elif choice == "4":
            if not books:
                print("Нет книг для отображения")
            for book in books:
                print(book.name)
                print('-'*30)

        else:
            print("Недопустимы выбор")



if __name__ == "__main__":
    main()

