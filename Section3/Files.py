from statistics import mode


myfile = open("E:\Python_udemy_course\Section3\myfile.txt")
print(myfile.read())  #reads the file
myfile.seek(0)  # When we read the file then the cursor comes at the last or EOF, so to read it again we use seek() to make the cursor move to 0.
print(myfile.readlines()) #returns a list of the string 

myfile.close()

#Another way for doing it

with open("E:\Python_udemy_course\Section3\myfile2.txt") as my_new_file:
    contents = my_new_file.read()
print(contents)

#Another way of doing it using the mode

with open("E:\Python_udemy_course\Section3\myfile2.txt",mode='r') as file: #reads the file
    content = file.read()
print(content)

#Writing into a file
with open("E:\Python_udemy_course\Section3\myfile2.txt",mode='w') as file2:
    pass

#Reading,Writing , Apppending Modes
#1. mode = 'r' is read only
#2. mode= 'w' is write only(will overwrite files or create new!)
#3. mode = 'a' is append only (will add on to files)
#4. mode = 'r+' is reading and writing
#5. mode = 'w+' is writing and reading (Overwrites existing files or create a new file!)

