#creating a class (a class functions as a template for an object)

class Book:     #self is a special parameter, must be included when initializing variables inside a class
                #variables in a class are referred to as instance variables
    
    #initializing the instance variables: 
    
    def __init__(self, pBooktitle, pBookauthor, pYearpublished):    
        self._title = pBooktitle                                    #always prefix instance variables with the self. keyword 
        self.author = pBookauthor                                   #these are the instance variables. The underscore before title is a convention.
        self.year = pYearpublished                                  #It warns coders not to directly access the variable because it has associated limiting properties.
        print ('creating a book file')

    def __str__ (self):
        return "Book Title: %s, Author: %s, Year Published: %d" %(self._title, self.author, self.year)
      
    #a procedure insisde a class is referred to as a method
    def calculateBookAge (self):
         self.age = 2018 - self.year
         return self.age

#to create an object in this class:
    
Book1 = Book ('Foundation', 'Asimov', 1948)                         #Python automatically includes the hidden self parameter
#The program returns 'creating a book file'

print (Book1)
#The program returns 'Book Title: Foundation, Author: Asimov, Year Published: 1946'

#to call the calculateBookAge method

Book1.calculateBookAge ()                                           #don't forget the parentheses
#The program returns 70

#To update any of the variables:
Book1.year = 1950
Book1.title = 'Foundation and Empire' 


#Adding properties:                                                 #Here I am pre-defining argument options for an instance variable
  
    @property                                                       #@property assigns a method to self.title (hidden procedure) 
    def title (self):
        print ('Fetching value')
        return self._title

    @title.setter                                                   #setter method: .setter is a pre-defined attribute to the property object
    def title (self, knownBook):
        if knownBook == 'Foundation' or knownBook == 'The Martian Way' or knownBook == 'Caves of Steel':
            self._title = knownBook
        else:
            print ('Are you sure he wrote that book? No changes made')





        
        
 
