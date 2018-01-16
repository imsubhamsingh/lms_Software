# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 19:35:44 2018

@author: Subham Singh
"""
#Basic software skeleton
'''
class Library:
    def __init__(self,listofbook):
        pass
    def displayAvailableBook(self):
        pass
    def lendBook(self):
        pass
    def addBook(self):
        pass

class Customer:
    def requestBook(self):
        pass
    def returnBook(self):
        pass
library = Library()
customer= Customer()
menu for user choice
'''
class Library:
    def __init__(self,listofbooks):
        self.availableBooks = listofbooks
        
    def displayAvailableBooks(self):
        print('')
        print('Available Books: ')
        for book in self.availableBooks:
            print(book)
    def lendBook(self,requestedBook):
        if requestedBook in self.availableBooks:
            print('Book Borrowed Successfully')
            self.availableBooks.remove(requestedBook)
        else:
            print('Book is not Available in library')
            
    def addBook(self,returnedBook):
        self.availableBooks.append(returnedBook)
        print('You have successfully retured the book')
        print('Thank you!')

class Customer:
    def requestBook(self):
        print('Please enter the name of book')
        self.book = input()
        return self.book
    def returnBook(self):
        print('Please enter the name of book')
        self.book = input()
        return self.book
 #object creation  
library = Library(['Harry Potter','Lord of the Ring','zero to one','2 States','Sherlock Holmes'])
customer= Customer()
#########Menu############################################
while True:
    print('****************************************')
    print('        Library Management System       ')
    print('****************************************')
    print('*  ENTER 1 TO DISPLAY AVAILABLE BOOKS  *')
    print('*  ENTER 2 TO REQUEST A BOOK 4         *')
    print('*  ENTER 3 TO RETURN A BOOK            *')
    print('*  ENTER 4 TO MEET DEVELOPER            *')
    print('*  Enter 5 TO MEET EXIT                *')
    print('****************************************')
    userchoice = int(input('->'))
    if userchoice is 1:
        library.displayAvailableBooks()
    elif userchoice is 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userchoice is 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userchoice is 4:
        print('He is the coolest geek bro.\n Feel free to contact on http://about.me/subhamsingh')
    elif userchoice is 5:
        exit()
##########End of program#################################
    
    


