class User(object):
    # Constructor
    def __init__(self, name, email):
        self.name = name # str
        self.email = email # str
        self.books = {} # empty dic
    # return email of the user
    def get_email(self):
        return self.email
    # update user's email
    def change_email(self, address):
        self.email = address
        print("%s's email has been changed to: %s" %(self.name, self.email))

    def __repr__(self):
        return "%s, email: %s, books read: %d" %(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        return False

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        ave = 0
        rated = 0
        for i in self.books.values():
            if i:
                ave += i
                rated += 1
        ave = ave/rated
        return ave

class Book(object):
    # Constructor
    def __init__(self, title, isbn):
        self.title = title #str
        self.isbn = isbn #number
        self.ratings = [] #empty list
    # get title of the book
    def get_title(self):
        return self.title
    # get isbn of the book
    def get_isbn(self):
        return self.isbn
    # set new isbn for the book
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("%s's ISBN has been changed to: %d" %(self.title, self.isbn))
    # add rating for the book
    def add_rating(self, rating):
        if rating and rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        return "Invalid Rating."
    # define comparision between books have same title and isbn
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        return False
    # get average rating of the book
    def get_average_rating(self):
        ave = 0
        rated = 0
        for i in self.ratings:
            if i:
                rated += 1
                ave += i
        ave = ave / rated
        return ave
    # hash method, used to compairng keys in dict during quick key lookup
    def __hash__(self):
        return hash((self.title, self.isbn))
# fiction books class
class Fiction(Book):
    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author
    # get the author of the book
    def get_author(self):
        return self.author
    # return a str
    def __repr__(self):
        return "%s by %s" %(self.title, self.author)
# non fiction books class
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "%s, a %s manual on %s" %(self.title, self.level, self.subject)
# TomeRater class
class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}
    # create book
    def create_book(self, title, isbn):
        n_book = Book(title, isbn)
        return n_book
    # create novel
    def create_novel(self, title, author, isbn):
        n_novel = Fiction(title, author, isbn)
        return n_novel
    # create non fiction book
    def create_non_fiction(self, title, subject, level, isbn):
        n_non_fiction = Non_Fiction(title, subject, level, isbn)
        return n_non_fiction
    # add book to user account
    def add_book_to_user(self, book, email, rating = None):
        n_user = self.users.get(email, None)
        if n_user:
            n_user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book] += 1
            book.add_rating(rating)
        else:
            print("No user with email %s" %(email))
    # add user with names, emails and books readed
    def add_user(self, name, email, books = None):
        n_user = User(name, email)
        self.users[email] = n_user
        if books:
            for i in books:
                self.add_book_to_user(i, email)
    # iterate through all keys in books and print out
    def print_catalog(self):
        for i in self.books:
            print (i)
    # iterate through all values of user and print out
    def print_users(self):
        for i in self.users.values():
            print (i)
    # iterate thorugh all books and return most readed book
    def most_read_book(self):
        max = float("-inf")
        most_read = None
        for i in self.books:
            readed = self.books[i]
            if readed > max:
                max = readed
                most_read = i
        return most_read
    # iterate through all books and find higest average rating
    def highest_rated_book(self):
        highest = float("-inf") # set maximum
        high_rate = None
        for i in self.books:
            ave = i.get_average_rating()
            if ave > highest:
                highest = ave
                high_rate = i
        return high_rate
    # iterate thorugh all users and find higest average rated user
    def most_positive_user(self):
        highest = float("-inf") # set maximum
        high_rate = None
        for i in self.users.values():
            ave = i.get_average_rating()
            if ave > highest:
                highest = ave
                hight_rate = i
        return hight_rate

    # check if email is been using
    def __hash__(self):
        return hash((self.email, self.isbn))
