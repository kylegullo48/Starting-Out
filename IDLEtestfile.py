

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
print (message2)
    


