import json
import os

class LibraryManager:
    def __init__(self):
        self.file = "library.txt"
        self.library = self.load_library()
        print(self.library)
    
    def load_library(self): # load library in self.library variable
        if os.path.exists(self.file):
            with open(self.file, 'r') as f:
                return json.load(f)
        return []

    def save_library(self): # update txt file
        with open(self.file, 'w') as f:
            json.dump(self.library, f)

    def add_book(self): # add book to the library and save into the file
        title = input('Enter the title of the book: ')
        author = input('Enter the author of the book: ')
        year = input('Enter the year of the book: ')
        genre = input('Enter the genere of the book: ')
        read = input('Have you read the book? (yes/no): ').lower() == 'yes'

        new_book = {
            'title' : title,
            'author' : author,
            'year' : year,
            'genre' : genre,
            'read' : read
        }

        self.library.append(new_book)
        self.save_library()
        print("-----------------")
        print(f"Book {title} added successfully.")
        print("-----------------")
    
    def remove_book(self):
        title = input("Enter the title book to remove from the library ")
        initial_length = len(self.library)
        self.library[:] = [book for book in self.library if book['title'].lower() != title]

        if len(self.library) < initial_length:
            self.save_library()
            print("-----------------")
            print(f"Book {title} removed successfully.")
            print("-----------------")
        else: 
            print("-----------------")
            print(f"Book {title} not found in the library.")
            print("-----------------")
    
    def search_library(self):
        search_by = input("Search by title or author ").lower()
        search_term = input(f"Enter the {search_by} ").lower()

        results = [book for book in self.library if search_term in book[search_by].lower()]

        if results:
            for book in results:
                status = "Read" if book['read'] else 'Unread'
                print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
        else:
            print("-----------------")
            print(f"No books found matching '{search_term}' in the {search_by} field.")
            print("-----------------")
    
    def display_all_books(self):
        if self.library:
            for book in self.library:
                status = "Read" if book['read'] else 'Unread'
                print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
        else:
            print("-----------------")
            print("The library is empty.")
            print("-----------------")
    
    def display_statistics(self):
        total_books = len(self.library)
        read_books = len([book for book in self.library if book['read']])
        percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

        print("-----------------")
        print(f"Total books: {total_books}")
        print(f"Percentage read: {percentage_read:.2f}%")
        print("-----------------")
    
    def display_menu(self):
        print("Welcome to the library manager.")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search the library")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

if __name__ == '__main__':
    libraryManager = LibraryManager()

    while True:
        libraryManager.display_menu()

        choice = input("Enter your choice: ")
       
        if choice == '1':
            libraryManager.add_book()
        elif choice == '2':
            libraryManager.remove_book()
        elif choice == '3':
            libraryManager.search_library()
        elif choice == '4':
            libraryManager.display_all_books()
        elif choice == '5':
            libraryManager.display_statistics()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")