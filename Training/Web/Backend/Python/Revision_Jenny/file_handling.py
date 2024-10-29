# File operations - open, read, write, close
# i. open function - returns a file obj or pointer/memory addr of the file
# e.g. my_file = open(filename, mode)
# where "mode" is the access mode of or type of operation to perform on the file such as,
# r(read), w(write), a(append), r+(read/write), w+(read/write), a+(read/append)
# x(create new file ifnotexist else, err)
# w(can also be used to create either file exist or not)

# f1 = open('file2.txt', 'x')
# f1 = open('file2', 'w')

# ii. READ file
# Throws error if file does not exist
# f1 = open('file2.txt', 'r')
f1 = open('IO_files/file1')   # 'r' is the default
print(f1.read())
print('-'*10)
f1.close()

# iii. WRITE file
# Overwrite the file content if already exist or create new one if not exist
# It keeps appending all the contents in the write functions
# of the current program
f2 = open('IO_files/file2', 'w')
# print(f2.read())  # Error: not readable
f2.write(">> 1. Hey!!! I am on \"write\" mode...")
f2.write(">> 2. Hey!!! I am on \"write\" mode...")
f2.close()

# IV. READ+WRITE or "r+" mode
# The process is "read before write"
# NB:-
# a. By default, the pointer/cursor is at the start of the file (0 position)
# b. write obj method - the pointer is at position 0
# c. read obj method - moves the pointer to end of file content
# * By following the usual "read before write" rule, the "w" method write
# at the end existing content
# * Else, it writes at the start of the existing content by overwriting required length for the
# * new content.
# Throws error if file does not exist
f3 = open('IO_files/file3', 'r+')
print(f3.tell())  # To know the position of the pointer
f3.write("Sodiq")
print(f3.tell())
f3.write("Ramon")
print(f3.tell())
print('"r+ mode"', f3.read())
print(f3.tell())
f3.write(">> Hey!!! I am on \"r+\" mode...")
f3.close()
print('-'*10)

# IV. WRITE+READ or "w+" mode
# The process is "write before read"  (opposite of "r+")
f4 = open('IO_files/file4', 'w+')  # Overwrite the existing on with no content
print(f4.tell())
f4.write('"w+ >> Number 1"')
f4.write('"w+ >> Number 2"')
f4.write('"w+ >> Number 3"')
f4.write('"w+ >> Number 3"')
print(f4.tell())
# print(f4.read())  # nothing is printed 'cos the pointer is at the end
f4.seek(0)  # Moves the pointer to the offset arg
print('*After seek method')
print(f4.tell())
print(f4.read())
print(f4.tell())
print('-'*10)

# V. APPEND or "a" mode
# Add new content at the end of a file (default) or create new one if not exist
# f5 = open('IO_files/file5', 'a')
# f5.write('This is from append mode')
# f5.read()  # Error
# print('-'*10)

# VI. APPEND & READ or "a+" mode
# In this case, the cursor/pointer/file handler is at the end of content
# And same goes to the "a" mode
f5 = open('IO_files/file5', 'a+')
print(f5.tell())
f5.read()

# VII. READ BINARIES (OTHER FILE TYPE ASIDE NORMAL TEXT)
# f6 = open('../../mr_lanx_1.jpg', 'r+')  # Error: can not decode it
f6 = open('../../mr_lanx_1.jpg', 'rb')
f7 = open('../../mr_lanx_2.jpg', 'ab')
# print(f6.read())

# To create new image by copy from the existing image
for i in f6:
    f7.write(i)




















