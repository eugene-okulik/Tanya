class Books:
    page_material = "бумага"
    is_text = True

    def __init__(self, title: object, author: object, number_of_pages: object, isbn_number: object,
                 is_reserve: object) -> None:
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn_number = isbn_number
        self.is_reserve = is_reserve

    def details_book(self):
        if self.is_reserve:
            print(
                f"Название: {self.title}, Автор: {self.author}, Страниц: {self.number_of_pages}, ISBN: {self.isbn_number}, "
                f"Материал: {Books.page_material}, Зарезервирована")
        else:
            print(
                f"Название: {self.title}, Автор: {self.author}, Страниц: {self.number_of_pages}, ISBN: {self.isbn_number}, "
                f"Материал: {Books.page_material}")


class SchoolBooks(Books):
    def __init__(self, title, author, number_of_pages, isbn_number, is_reserve, subject, class_room, is_exercises):
        super().__init__(title, author, number_of_pages, isbn_number, is_reserve)
        self.subject = subject
        self.class_room = class_room
        self.is_exercises = is_exercises

    def details_school_book(self):
        if self.is_reserve:
            print(
                f"Название: {self.title}, Автор: {self.author}, Страниц: {self.number_of_pages}, Предмет: {self.subject}, "
                f"Класс: {self.class_room}, Зарезервирована")
        else:
            print(
                f"Название: {self.title}, Автор: {self.author}, Страниц: {self.number_of_pages}, Предмет: {self.subject}, "
                f"Класс: {self.class_room}")


obj1 = SchoolBooks("Алгебра", "Иванов", 200, None, True,
                   "Математика", 9, True)
obj2 = SchoolBooks("История мира", "Петрухин", 100, None, False,
                   "История", 8, False)

obj1.details_school_book()
obj2.details_school_book()
