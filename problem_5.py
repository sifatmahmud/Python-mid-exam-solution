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

    @classmethod
    def borrow_book(cls, book_id, book_title):
        for book in Book.book_list:
            if book['id'] == book_id and book['title'] == book_title:
                if book['availability']==True:
                    book['availability'] = False
                    break

    @classmethod
    def return_book(cls,book_id, book_title):
        for book in Book.book_list:
            if book['id'] == book_id and book['title'] == book_title:
                if book['availability'] == False:
                    book['availability'] = True
                    break




# -------------------- main area -----------------------
book1 = Book(101, 'physics', 'Albert')
book2 = Book(102, 'biology', 'Newton')


