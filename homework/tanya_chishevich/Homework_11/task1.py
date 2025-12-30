class Books:
    page_material = "бумага"
    is_text = True

    def __init__(self, title, author, number_of_pages, isbn_number, is_reserve):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn_number = isbn_number
        self.is_reserve = is_reserve

    def details_book(self):
        if self.is_reserve:
            print(f"Название: {self.title}, Автор: {self.author}, Страниц: {self.number_of_pages}, "
                  f"ISBN: {self.isbn_number}, Материал: {Books.page_material}, Зарезервирована")
        else:
            print(
                f"Название: {self.title}, Автор: {self.author}, Страниц: {self.number_of_pages}, "
                f"ISBN: {self.isbn_number}, Материал: {Books.page_material}")


obj1 = Books("Идиот", "Достоевский", 500, 56778, False)
obj2 = Books("Отцы и дети", "Онегин", 300, 54682, False)
obj3 = Books("Ася", "Тургенев", 455, 67895, True)
obj4 = Books("Анна Каренина", "Толстой", 600, 67894, False)
obj5 = Books("Собачье сердце", "Булгаков", 633, 67432, False)

obj1.details_book()
obj2.details_book()
obj3.details_book()
obj4.details_book()
obj5.details_book()
