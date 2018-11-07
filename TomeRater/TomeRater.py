class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        print("This Users email is" + self.email)

    def change_email(self, address):
        self.email = address
              
        return "This user's email has been updated to " + self.email + "."
        
    def __repr__(self):
        return "User: " + self.name + ", Email: " + self.email + ", Number of books read: " + str(len(self.books)) + "."
 
    def __eq__(self, other_user):
        if other_user.name == self.name and other_user.email == self.email:
            return True
        else:
            return False

    def read_book(self,book,rating=None):

        self.books[book] = rating

    def get_average_rating(self):
        
        rating_list = []
        average = 0
        
        for rating in self.books.values():
            if rating != None:
                rating_list.append(rating)

        for i in rating_list:
            average += i
            
        if len(rating_list) > 0:
            final_average = average / len(rating_list)
            return final_average
        else:
            return average
        
        
class Book(object):

    def __init__(self,title,isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        

    def __repr__(self):
        return "Title: " + self.title +"," + " ISBN: " + str(self.isbn) + "."

    def get_title(self):
        return "The title of this book is " + self.title + "."

    def get_isbn(self):
        return "The ISBN number of this book is " + str(self.isbn) + "."

    def set_isbn(self,new_isbn):
                
        return print("This book's ISBN number has been updated to " + str(new_isbn) + ".")

    def add_rating(self,rating):
        
        if rating:
            if rating > 0 and rating <= 4:
               self.ratings.append(rating)

            else:
                print("Invalid Rating")
  
    def __eq__(self,other_book):

        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def	__hash__(self):
        return hash((self.title,self.isbn))

    def get_average_rating(self):

        rating = 0
            
        for i in self.ratings:
            rating += i
        
        average_rating = rating / len(self.ratings)
        return average_rating

        

class Fiction(Book):
    def __init__(self,title,author,isbn):
        super().__init__(title,isbn)
        self.author = author

    def get_author(self):
        return "The author of this book is: " + self.author + "."

    def __repr__(self):
        return self.title + " by " + self.author + "." 


class NonFiction(Book):
    def __init__(self,title,subject,level,isbn):
        super().__init__(title,isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return "The subject of this book is " + self.subject + "."

    def get_level(self):
        return "The level of this book is " + self.level + "."

    def __repr__(self):
        return self.title + ", " + self.level + " manual on " + self.subject + "."


class TomeRater(object):

    def __init__(self):
        self.users = {}
        self.books = {}
        self.isbn_list = []
        

    def create_book(self,title,isbn):

        if isbn in self.isbn_list:
            print ("Error. This isbn already exists.")
            
        new_book = Book(title,isbn)

        self.isbn_list.append(isbn)
        
        return new_book

    def create_novel(self,title,author,isbn):

        if isbn in self.isbn_list:
            print ("Error. This isbn already exists.")
            
            
        new_novel = Fiction(title,author,isbn)

        self.isbn_list.append(isbn)

        return new_novel

    def create_non_fiction(self,title,subject,level,isbn):

        if isbn in self.isbn_list:
            print ("Error. This isbn already exists.")
            
        new_non_fiction = NonFiction(title,subject,level,isbn)

        self.isbn_list.append(isbn)

        return new_non_fiction
    
    
    def set_isbn(self,book,new_isbn):

        for isbn in self.isbn_list:
            if isbn == book.isbn:
                self.isbn_list.remove(isbn)

        self.isbn_list.append(new_isbn)
                
        return print("This book's ISBN number has been updated to " + str(new_isbn) + ".")
    

    def get_list_of_isbn(self):

        #returns a list of all the isbn numbers stored in TomeRater

        return self.isbn_list


    def add_book_to_user(self,book,email,rating=None):

        if email in self.users.keys():
            
            self.users[email].read_book(book,rating)
            
            book.add_rating(rating)
            
            if book not in self.books.keys():
                self.books[book] = 1

            else:
                self.books[book] += 1
        else:
           print("No user with email {email}!".format(email=email))
           
    
    def add_user(self,name,email,user_books=None):

        if email in self.users.keys():
            print("This user already exists.")

        user = User(name,email)
        self.users[email] = user

        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book,email)

        return user        
                
    def print_catalog(self):

        for key in self.books.keys():
            print(key)

    def print_users(self):

        for value in self.users.values():
            print(value)
    
    def get_most_read_book(self):
        
        maximum_value = max(self.books.values())

        for key,value in self.books.items():
            if value == maximum_value:
                return key

   
    def highest_rated_book(self):

        average_rating_list = []


        for book in self.books.keys():
            
            average_rating = book.get_average_rating()
            average_rating_list.append(average_rating)

        max_rating = max(average_rating_list)

        for book in self.books.keys():
            
            average_rating = book.get_average_rating()
            if average_rating == max_rating:
                return book
        
            
    def most_positive_user(self):

        average_rating_list = []

        for key,value in self.users.items():
            
            average_rating = value.get_average_rating()
            average_rating_list.append(average_rating)
            
        max_rating = max(average_rating_list)

        for key,value in self.users.items():
            
            average_rating = value.get_average_rating()
            if average_rating == max_rating:
                return value
            
            
            

         







    




