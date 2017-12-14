'''
Write a Python program that performs the following tasks:
1. Create a Python class that stores information about a book. This information includes:
Book Title
Book Publisher
Publication Year
Book Price
Book Category (fiction/non-fiction)
2. Create a loop to prompt the user for book information and use this to create instances of the
Book Class and store each instance in a Python List.
3. After the user leaves the Book Input loop, for each item in the Book List, print out the book title
and book price.
'''

class bookClass(object):
    def __init__(self,a,b,y,p,cat):
        self.title = a
        self.publisher = b
        self.year = y
        self.price = p
        self.category = cat

    def getTitle(self):
        return self.title

    def getPublisher(self):
        return self.publisher

    def getYear(self):
        return self.year

    def getPrice(self):
        return self.price

    def getCategory(self):
        return self.category
#################################Customer Input#############

Continue = True
booklist = []
while Continue:
    btitle = input("Pleas eenter book title:")
    bpublisher = input("Pleas eenter book publisher:")
    byear = input("Pleas eenter book year:")
    bprice = input("Pleas eenter book price:")
    bcategory = input("Pleas eenter book Category:")

    ####Form class and keep in a lsit##################
    b1 = bookClass(btitle,bpublisher,byear,bprice,bcategory)
    booklist.append(b1)

    ##########Want to continue?#####################
    YesorNo = input("Do you want to continue? ")
    if (str(YesorNo.lower()) == "y"):
        Continue = True
    else:
        Continue = False


###########Print the list of books###############
print ("Number of books are : ",len(booklist))
print ("######Your Book List#############")
for x in booklist:
    print ("The book title is:  ",x.getTitle())
    print (" the Book publisher is: ", x.getPublisher())
    print("The book published year is:  ", x.getYear())
    print("The book price is:  ", x.getPrice())
    print("The book category  is:  ", x.getCategory())
    print ("######Next book##########sdf")



