class Book:
    def __init__(self, title, author, pages, publication_year):
        self.title = title
        self.author = author
        self.pages = pages
        self.publication_year = publication_year

    def get_summary(self):
        return f"{self.title} by {self.author}, published in {self.publication_year} with {self.pages} pages."

    def get_author(self):
        return self.author

# Create a Book instance
book = Book("How to be romatic", "Isaac Xavier", 451, 1900)

# Print the book summary
print(book.get_summary())

# Print the author
print(book.get_author())