import csv
global header
global data
global file_name

header = ['ID', 'Type', 'Status', 'Price', 'Size', 'Description', 'Favorite']
data = []
file_name = 'documents/user_data.csv'
#file_name = 'documents/test.csv'

def read_data():
    global data
    data = []
    with open(file_name, 'r', newline='') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            data.append(row)

def write_row(input):
    import csv
    with open(file_name, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(input)
        f.close()

def append_data(type, status, price, size, description, favorite):
    y = generateID()
    x = [y, type, status, price, size, description, favorite]
    data.append(x)
    write_row(x)
    return y



def generateID():
    import random
    import string
    list = []
    for i in range(4):
        list.append(random.choice(string.ascii_letters))
    list.append(str(random.randint(0,9)))
    aaa = ""
    for item in list:
        aaa = aaa+item
    return aaa

def getlistoflists():
    import csv

    class clothesitem:
        def __init__(self, ID, type, status, price, size, description, favorite):
            self.ID = ID
            self.idimagename = str(ID) + ".png"
            self.type = type
            self.status = status
            self.price = price
            self.size = size
            self.description = description
            self.favorite = favorite

    ls = []

    with open('documents/user_data.csv') as file_obj:
        readerobj = csv.reader(file_obj)
        for row in readerobj:
            m = []
            if row != []:
                row[0] = str(row[0]) #ID
                row[1] = str(row[1]) #shirt or dress or bag or whatever
                row[2] = str(row[2]) #washed or dirty
                row[3] = float(row[3]) #price
                row[4] = str(row[4]) #size
                row[5] = str(row[5]) #description
                row[6] = bool(row[6]) #favorite true or false

                ls.append(row)

        print(ls)
        return(ls)

#append_data(generateID(), "shirt", "washed", 40.0, "small", "cool shirt", False)
