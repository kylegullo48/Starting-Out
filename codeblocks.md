I am using this file to learn how to import multiple sections of code into a git file and comment on them. I want the finished product to be a user-friendly, easily readable page with small sections of code demonstration. 

To do that, I have to create and highlight code blocks in markdown. There's a help page that shows you how to do it [here](https://help.github.com/articles/creating-and-highlighting-code-blocks/). I'm writing in a Markdown file on my desktop, then uploading to my Git repository. 

For my purposes, I'm using a demo of how inheritance works in Python. It's taken from the book [Learn Python in one day](https://www.amazon.com/Python-Beginners-Hands-Project-Project-ebook/dp/B00R9JPDN4). 

I want to create a new class which is the same as an existing class – its parent – with some modifications. 
Here's the parent class. You'll also hear this called a super class, or base class: 

```Python
class Staff:
    def __init__ (self, pPosition, pName, pPay):
        self._position = pPosition
        self.name = pName
        self.pay = pPay
        print ('Creating Staff object')
```
The __init__ method initializes the instance variables \_position, name and pay. 

The following methods also belong to the Staff class. __str__ is a special method used to return a string that represents the class. The calculatePay method makes use of some instance variables common to the class (prefixed by self.) It also uses local variables. 

```Python
    def __str__ (self):
        return "Position = %s, Name = %s, Pay = %d" %(self._position, self.name, self.pay)

    def calculatePay (self):
        prompt = '\nEnter number of hours worked for %s: ' %(self.name)
        hours = input (prompt)
        prompt = 'Enter the hourly rate for %s: ' %(self.name)
        hourlyRate = input (prompt)
        self.pay = int (hours)*int (hourlyRate)
        return self.pay
```        
Properties set some limitations on the parameters for the instance variable \_position: 

```Python
    @property
    def position (self):
        print ("Getter Method")
        return self._position

    @position.setter
    def position (self, value):
        if value == 'Manager' or value == 'Basic':
            self._position = value
        else:
            print ('position is invalid. No changes made.')
```
A child of the Staff class inherits all the variables and methods in that class and adds some of its own. 
```Python
class ManagementStaff (Staff):

    def __init__(self, pName, pPay, pAllowance, pBonus):
        super ().__init__('Manager', pName, pPay)
        self.allowance = pAllowance
        self.bonus = pBonus
```
It can also override parts of the parent class with its own methods.  
```Python
    def calculatePay (self):
        basicPay = super ().calculatePay ()
        self.pay = basicPay + self.allowance 
        return self.pay
```
That's the end of the demo. If reading the code above was not easy, I recommend getting the book. It takes you through each line of code and explains how it works in detail. This is a stripped down version of what you will find there. 
