# Class that declares books
class BookSales():
    # Variables to be identical when instanced
    cutOfProfit = 0.6

    # Variables to be defined when instanced
    def __init__(self, sales, price):
        self.sales = sales
        self.price = price
        self.gross = self.price * self.cutOfProfit
        self.profit = self.gross * self.sales
    
    def __str__(self):
        return "This is the 'BookSales' class"
    
    def __repr__(self):
        return "BookSales()"

# Class that declares book instance details
class NewBook():
    # Variables to be defined when instanced
    def __init__(self, title, pageNum, genre, sales, price):
        self.title = title
        self.pageNum = pageNum
        self.genre = genre
        self.__salesDetails = BookSales(sales, price)
        self.__profit = self.__salesDetails.profit

    # __str__ function: returns the below string when the object itself is passed into the 'print' function
    def __str__(self):
        return "This is the 'NewBook' class"

    # __repr__ function: returns the below string when the object itself is passed is called by itself
    def __repr__(self):
        return "NewBook()"

    # Print the title and genre of book
    def printBookDetails(self):
        print("The title of this book is '" + self.title, "', and is of the genre '" + self.genre + "'.")

    # Prints the length of the book
    def printBookLength(self):
        if self.pageNum < 100:
            print("This is a short book, only " + str(self.pageNum) + " pages.")
        elif self.pageNum <= 300:
            print("This is a moderately long book, " + str(self.pageNum) + " pages.")
        else:
            print("This is a LONG book, a whooping " + str(self.pageNum) + " pages!")
    
    # Add book to library
    def addToLibrary(self, library):
        library.listOfBooks.append(self)
        print("'" + self.title + "' is now available at " + library.libraryName + ".")