
class Book:
    def __init__(self, pBooktitle, pBookauthor, pYearpublished):
        self.title = pBooktitle
        self.author = pBookauthor
        self.year = pYearpublished
        print ('creating a book file')

    def __str__ (self):
        return "Book Title: %s, Author: %s, Year Published: %d" %(self.booktitle, self.bookauthor, self.yearpublished)

    
