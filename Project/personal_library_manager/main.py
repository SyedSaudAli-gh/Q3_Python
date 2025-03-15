import json

class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their reading materials."""

    def __init__(self):
        """Initialize a new book collection with an empty list and set up file storage."""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()
        
    def read_from_file(self):
        """Load saved books from a json file into memory.
        If the file doesn't exist or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []
            
    def save_to_file(self):
        """Store the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)
            
    def create_new_book(self):
        """Add a new book to the collection by gathering information from the user."""
        book_title = input("Enter book title: ")
        book_author = input("Enter author name: ")
        publication_year = input("Enter publication year: ")
        book_genre = input("Enter book genre: ")
        is_book_read = input("Have you read this book? (yes/no):").strip().lower() == "yes"

        new_book = {
            "title" : book_title,
            "author" : book_author,
            "year" : publication_year,
            "genre" : book_genre,
            "read" : is_book_read,
        }
        
        self.book_list.append(new_book)
        self.save_to_file()
        print(f"Book '{book_title}' has been added to your collection Successfully!\n")
        
    def delete_book(self):
        """Remove a book from the collention using the title"""
        book_title = input("Enter the title of the book to remove: ")
        
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print(f"Book {book_title} removed successfully!\n")
                return
        print(f"\nBook with title '{book_title}' not found in your collection.\n")
        
        
    def find_book(self):
        """Search for books in the collection bt title and author name."""
        search_type = input("Search by: \n1. Title\n2. Author\nEnter your choice: ")
        search_text = input("Enter Search term: ").lower()
        found_books = [
            book for book in self.book_list
            if search_text in book["title"].lower() or search_text in book["author"].lower()
        ]
        
        if found_books:
            print("Matching Books: ")
            for index, book in enumerate(found_books, start=1):
                reading_status = "Read" if book["read"] else "unread"
                print(f"{index}. {book['title']} - {book['author']} ({book['year']}) - {reading_status}")
        else:
            print("No matching books found\n.")
            
    def update_book(self):
        """Modify the details of an existing book in the collection."""
        book_title = input("Enter the title of the book you want to edit: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = input(f"New author ({book['author']}): ") or book["author"]
                book["year"] = input(f"New publication year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                book["read"] = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
                
                self.save_to_file()
                print(f"Book '{book_title}' updated successfully!\n")
                return
        print(f"\nBook with title '{book_title}' not found in your collection.\n")
        
    def show_all_books(self):
        """Display all books in the collection with their details."""
        if not self.book_list:
            print(" Your collection is empty.\n")
            return
        
        print("Your Book Collection:")
        for index, book in enumerate(self.book_list, start=1):
            reading_status = "Read" if book["read"] else "unread"
            print(f"{index}. {book['title']} - {book['author']} ({book['year']}) - {reading_status}")
        
    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (
            (completed_books / total_books * 100) if total_books > 0 else 0
        )
        print(f"Total books in collection: {total_books}")
        print(f"Reading progress: {completion_rate:.2f}%\n")
        
        
    def start_application(self):
        """Run the main application loop with a user_friendly interface."""
        while True:
            print("📚 Welcome to the Book Collection Manager! 📚")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")
            user_choice = input("Please choose an option (1-7): ")
            
            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.show_all_books()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        
                

if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()
