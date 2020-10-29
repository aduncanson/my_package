# Create library
myLibrary = Packages.library.Library()

# Create some clients
alex = Packages.people.AddClient("Alex", "Billson", 23, "male", "1 First Street")
bill = Packages.people.AddClient("Bill", "Charles", 53, "male", "2 Second Street")
chris = Packages.people.AddClient("Chris", "Downs", 35, "male", "3 Third Street")
dylan = Packages.people.AddClient("Dylan", "Everton", 19, "male", "4 Fourth Street")

# Create some employees
eve = Packages.people.AddEmployee(myLibrary, "Eve", "Fry", 41, "female", "5 Fifth Street", 10)
freya = Packages.people.AddEmployee(myLibrary, "Freya", "Greggs", 20, "female", "6 Sixth Street", 9)
georgia = Packages.people.AddEmployee(myLibrary, "Georgia", "Holmes", 30, "female", "7 Seventh Street", 9)
hanna = Packages.people.AddEmployee(myLibrary, "Hanna", "Ivory", 34, "female", "8 Eighth Street", 8)

# Add client to library
eve.addToLibrary(myLibrary)
freya.addToLibrary(myLibrary)
georgia.addToLibrary(myLibrary)
hanna.addToLibrary(myLibrary)

# Create some books
hobbit = Packages.book.NewBook("The Hobbit", 200, "Fantasy", 1000000, 12)
fellowship = Packages.book.NewBook("The Fellowship", 534, "Fantasy", 836200, 12)
twoTowers = Packages.book.NewBook("The Two Towers", 496, "Fantasy", 648300, 12)
returnKing = Packages.book.NewBook("The Return", 817, "Fantasy", 884600, 12)

# Clients check out some books
alex.checkOutBook(hobbit)
bill.checkOutBook(fellowship)
chris.checkOutBook(twoTowers)
dylan.checkOutBook(returnKing)

# Employees check out some books
eve.checkOutBook(hobbit)
freya.checkOutBook(hobbit)
georgia.checkOutBook(hobbit)
hanna.checkOutBook(hobbit)
eve.checkOutBook(fellowship)
freya.checkOutBook(fellowship)
georgia.checkOutBook(fellowship)
hanna.checkOutBook(fellowship)

# Employees check in some books
eve.checkBookBackIn(hobbit)
freya.checkBookBackIn(hobbit)
georgia.checkBookBackIn(hobbit)
hanna.checkBookBackIn(hobbit)

# List all clients, employees, and books in Library object
myLibrary.generateListOfClient()
myLibrary.generateListOfEmployees()
myLibrary.generateListOfBooks()

# Call one method from each class
myLibrary.printTheOwners()
alex.printPreviouslyCheckedOutVolume()
eve.promoteEmployee()
hobbit.printBookLength()