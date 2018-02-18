I am using this file to learn how to import multiple sections of code into a git file and comment on them. I want the finished product to be a user-friendly, easily readable page with small sections of code demonstration. 

To do that, I have to create and highlight code blocks in markdown. There's a help page that shows you how to do it [here](https://help.github.com/articles/creating-and-highlighting-code-blocks/)

Here's a demo of how inheritance works in Python. It's taken from the book [Learn Python in one day](https://www.amazon.com/Python-Beginners-Hands-Project-Project-ebook/dp/B00R9JPDN4)

First, let's create the parent class. You'll also hear this called a super class, or base class: 

```
class Staff:
    def __init__ (self, pPosition, pName, pPay):
        self._position = pPosition
        self.name = pName
        self.pay = pPay
        print ('Creating Staff object')
```
