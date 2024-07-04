class Book:
    def __init__(self, title,pages):
        self.title = title
        self.pages = pages
    
    def isLong(self,pages):
        if self.pages > 100:
            return True
        return False
    
    def __str__(self):
        return f"{self.title} {self.pages}"


book1 = Book("Hello Tom",24)

del book1

print(book1.pages)





