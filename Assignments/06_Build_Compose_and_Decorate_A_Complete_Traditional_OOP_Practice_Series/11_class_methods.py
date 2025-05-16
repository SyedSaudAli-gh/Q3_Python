class Book:
    total_books = 0
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"count a new book is {cls.total_books}")
        

Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()