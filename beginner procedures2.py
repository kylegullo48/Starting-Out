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




#buffering procedure:

inputFile = open ('daysofweek', 'r')
outputFile = open ('daysoutput', 'w')

#read function specifies the buffer size, msg reads 4 bytes at a time:

msg = inputFile.read (4)

#following procedure loops through the file 4 bytes at a time
#while is conditional on msg having length, it stops when msg has no bytes

while len (msg):
    outputFile.write (msg + '\n')  #newline to show in the printout that the 4 byte buffering worked
    msg = inputFile.read(10)

outputFile.close ()
outputFile = open ('daysoutput', 'r+')

for line in outputFile:
    print (line, end = '')

inputFile.close ()
outputFile.close ()




#buffering procedure adapted to read and create an external binary file:

inputFile = open ('myWallaby.jpeg', 'rb')
outputFile = open ('myWallabyOutput.jpeg', 'wb')


#read function specifies the buffer size, msg reads 10 bytes at a time:

msg = inputFile.read (10)

while len (msg):
    outputFile.write (msg)  
    msg = inputFile.read(10)

inputFile.close ()
outputFile.close ()



#rename

import os as os
os.rename ('daysofweek', 'weekdays')

#remove only removes one file at a time

os.remove ('test.py')



