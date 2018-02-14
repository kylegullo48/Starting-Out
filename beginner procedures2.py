'''
created a procedure to open an external txt file
started using Visual Studio Code to create txt & source code files
'daysofweek' is ref to the external .txt file
'''

f = open ('daysofweek', 'r')

firstline = f.readline()
secondline = f.readline()
print (firstline)
print (secondline)

f.close()

