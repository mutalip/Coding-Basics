'''

Write a Python program that performs the following tasks:
1. Prompt the user for their first name, last name, and address (street, city, state, and zip).
2. Prompt the user for a file name.
3. Open a file with the file name supplied by the user and write the user information to the file.
4. Close the file.
5. Reopen the file for input and read back all the information.
6. Print the information read from the file to the screen.


'''

firstname=  input("please inter your first name: ")
lastname = input("please inter your last name: ")
address = input("please inter your address: ")
filename = input("please inter file name: ")
filename = filename + ".txt"



fo = open(filename, "w")
fo.write(firstname)
fo.write("\n")
fo.write(lastname)
fo.write("\n")
fo.write(address)
fo.write("\n")
fo.close()

fo = open(filename, "r")
str = fo.readlines()
print (str)
fo.close()
