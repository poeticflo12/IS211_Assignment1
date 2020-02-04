class Book:
    def __init__(self, author="", title=""):
        self.author = author
        self.title = title

    def display(self):
        print(self.title + ", Written by " + self.author)


book0 = Book("John Steinbeck", "Of Mice and Men")
book1 = Book("Harper Lee", "To Kill a Mockingbird")
book0.display()
book1.display()

