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

#using a for loop instead of readline to access, append and print text from an external file:

f = open ('daysofweek', 'r+')
for line in f:
    print (line, end = '')

f.close ()


g = open ('daysofweek', 'a')
g.write ('\nSaturday' '\nSunday')
g.close ()


h = open ('daysofweek', 'r+')
for line in h:
    print (line, end = '')
h.close ()


