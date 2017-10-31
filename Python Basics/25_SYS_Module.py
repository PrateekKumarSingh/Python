import sys 

# import sys 
# help(sys) to know more about the system module

# Dynamic Objects
sys.stderr.write('this is stderr text\n') # stderr -- standard error object; used for error messages
sys.stderr.flush()
sys.stdout.write('this is stdout text\n') # stdout -- standard output file object; used by print()

print(sys.argv) # prints command line arguments passed to the program
print(len(sys.argv),"argument(s) passed to the script") # len(sys.argv) to count Number of arguments
if len(sys.argv)>1:
    print(sys.argv[1] * 3)  # Perform operations on the arguments

print(sys.path)  # A list of strings that specifies the search path for modules. Initialized from the environment variable PYTHONPATH,
print(sys.modules)  # This is a dictionary that maps module names to modules which have already been loaded. This can be manipulated to force reloading of modules and other tricks.
print("Platform:",sys.platform) # platform identifier, like Win32

print("Python interpreter v",sys.winver)

# sys.argv are the Arguments passed to python program like, in the following example
# python.exe c:/Data/Python/Scripts/python/25_Using_System_Module.py "This is an argument"
# this is stderr text
# this is stdout text
# ['c:/Data/Python/Scripts/python/25_Using_System_Module.py', 'This is an argument']
