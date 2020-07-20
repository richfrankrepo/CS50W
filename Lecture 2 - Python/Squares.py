#import the function 'square' from the file/module 'Functions'
from Functions import square

#Call the 'square' function from the 'Functions' file for the values 0 to 14
for i in range(15):
    print(f"The square of {i} is {square(i)}")


# alternativley, we could import the whole functions file, then qualify the function call as follows..
#   import Functions
#   print(f"The square of {i} is {functions.square(i)}")