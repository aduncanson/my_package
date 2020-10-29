# Class that declares client instance details
class AddClient():
    # Variables to be identical when instanced
    previouslyCheckedOutBooks = []
    activelyCheckedOutBooksList = []

    # Variables to be defined when instanced
    def __init__(self, firstName, surname, age, gender, address):
        self.__firstName = firstName
        self.surname = surname
        self.age = age
        self.gender = gender
        self.address = address
        self.fullName = self.__firstName + " " + self.surname

    # __str__ function: returns the below string when the object itself is passed into the 'print' function
    def __str__(self):
        return "This is the 'AddClient' class"

    # __repr__ function: returns the below string when the object itself is passed is called by itself
    def __repr__(self):
        return "AddClient()"
    
    # Prints the clients name
    def printName(self):
        print("The client is called " + self.fullName + ".")
    
    # Prints the number of books checked out by the client
    def printPreviouslyCheckedOutVolume(self):
        if len(self.previouslyCheckedOutBooks) == 1:
            print("The client has checked out " + str(len(self.previouslyCheckedOutBooks)) + " book in the past.")
        else:
            print("The client has checked out " + str(len(self.previouslyCheckedOutBooks)) + " books in the past.")
    
    # Prints the names of the books currently checked out by the client
    def printActivelyCheckedOut(self):
        print(self.fullName + "currently has these books checked out:")
        for ind, book in enumerate(self.activelyCheckedOutBooksList):
            print("  Book " + str(ind + 1) + ": " + book.title)

    # Prints the clients age
    def printAge(self):
        if self.gender == "male":
            print("He is " + str(self.age) + " years old.")
        elif self.gender == "female":
            print("She is " + str(self.age) + " years old.")
        else:
            print("They are " + str(self.age) + " years old.")
    
    # Add book to clients checked out list
    def checkOutBook(self, newBook):
        self.activelyCheckedOutBooksList.append(newBook)
        print("'" + newBook.title + "' has been added to " + self.fullName + "'s checked out list.")

    # Remove book from clients checked out list and adds to their historic list
    def checkBookBackIn(self, newBook):
        self.activelyCheckedOutBooksList.remove(newBook)
        print("'" + newBook.title + "' has been removed from " + self.fullName + "'s checked out list.")
        self.previouslyCheckedOutBooks.append(newBook)
        print("'" + newBook.title + "' has been added to " + self.fullName + "'s historic checked out list.")
    
    # Add client to library
    def addToLibrary(self, library):
        library.listOfClients.append(self)
        print("'" + self.fullName + "' is now a member of " + library.libraryName + ".")

# Class that declares employee instance details
class AddEmployee(AddClient):
    # Variables to be identical when instanced
    previouslyCheckedOutBooks = []
    activelyCheckedOutBooksList = []

    # Variables to be defined when instanced
    def __init__(self, library, firstName, surname, age, gender, address, employeeLevel):
        super().__init__(firstName, surname, age, gender, address)
        self.employeeLevel = employeeLevel
        library.listOfEmployees.append(self)

    # __str__ function: returns the below string when the object itself is passed into the 'print' function
    def __str__(self):
        return "This is the 'AddEmployee' class"
    
    # __repr__ function: returns the below string when the object itself is passed is called by itself
    def __repr__(self):
        return "AddEmployee()"
    
    # Prints the employees name
    def printName(self):
        print("The employee is called " + self.fullName + ".")
    
    # Promotes the employees to the next level
    def promoteEmployee(self):
        self.employeeLevel = self.employeeLevel + 1
        print("The employee has been promoted from level " + str(self.employeeLevel - 1) + " to level " + str(self.employeeLevel) + ".")