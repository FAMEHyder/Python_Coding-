# time module in python

import time
timestamp = time.strftime('%H:%M:%S')

print (timestamp)

timestamp = int (time.strftime('%H'))

print (timestamp)

timestamp = int (time.strftime('%M'))

print (timestamp)

timestamp = int (time.strftime('%S'))

print (timestamp)


if (int (time.strftime('%H')<12)):
    if (int (time.strftime('%M')<=0)):
        if (int (time.strftime('%S')<=00)):
            print ("good morning")

else :
    print ("sorry")