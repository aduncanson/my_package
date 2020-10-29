# Class that declares library instance details
class Library():
    # Variables to be identical when instanced
    listOfClients = []
    listOfEmployees = []
    listOfBooks = []
	
    # Variables to be defined when instanced
    def __init__(self, libraryOwner=None, libraryCoowner=None, libraryName=None):
        # If the libraryOwner isn't populated, then use the default value
        if libraryOwner is None:
            self.libraryOwner = "Dylan Scott"
        else:
            self.libraryOwner = libraryOwner
        
        # If the libraryCoowner isn't populated, then use the default value
        if libraryCoowner is None:
            self.libraryCoowner = ""
        else:
            self.libraryCoowner = libraryCoowner
        
        # If the libraryName isn't populated, then use the default value
        if libraryName is None:
            self.libraryName = "Durham Books!"
        else:
            self.libraryName = libraryName
	
    # __str__ function: returns the below string when the object itself is passed into the 'print' function
    def __str__(self):
        return "This is the 'BookPublisher' class"
    
    # __repr__ function: returns the below string when the object itself is passed is called by itself
    def __repr__(self):
        return "BookPublisher()"
    
    # Prints the owner(s) of the Library
    def printTheOwners(self):
        if self.libraryCoowner == "":
            print("The owner of '" + self.libraryName + "' is " + self.libraryOwner + ".")
        else:
            print("The owners of '" + self.libraryName + "' are " + self.libraryOwner + " and " + self.libraryCoowner + ".")
    
    # Print out a list of all clients of the library
    def generateListOfClient(self):
        print("List of all clients:")
        clientList = list(dict.fromkeys(self.listOfClients))
        for client in clientList:
            print("  " + client.fullName)
    
    # Print out a list of all employees of the library
    def generateListOfEmployees(self):
        print("List of all employees:")
        employeeList = list(dict.fromkeys(self.listOfEmployees))
        for employee in employeeList:
            print("  " + employee.fullName)
    
    # Print out a list of all books in the library
    def generateListOfBooks(self):
        print("List of all books:")
        bookList = list(dict.fromkeys(self.listOfBooks))
        for book in bookList:
            print("  " + book.title)