class Library:
    book_list = []


    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)


class Book(Library):

    def __init__(self, book_id, title, author, availability = True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability

        book_details = {"id" : self.__book_id, "title" : self.__title, "author" : self.__author, "availability" : self.__availability}

        self.entry_book(book_details)

# -------------------- main area -----------------------
book1 = Book(101, 'physics', 'Albert')
book2 = Book(102, 'biology', 'Newton')




