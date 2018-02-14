'''
this is a random .py file that I was using to test some simple functions
I'm using it to test an upload to git, to see if the color coding in IDLE is retained 
it turns out that some of it is - enough to be useful
'''

def primeOrNot (numberToCheck):
    for x in range (2, numberToCheck):
        if (numberToCheck%x == 0):
            return False
        return True

    

message1 = "global variable"

def myFunction ():
    print ("\nINSIDE THE FUNCTION")
    print (message1)
    message2 = "local variable"
    print (message2)


myFunction ()

print ("\nOUTSIDE THE FUNCTION")
print (message1)

    


