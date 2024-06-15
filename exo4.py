#index error

def access_list_element(lst,index):
    try:
        value=lst[index]
        print("Value at index",index,"is",value)
    except IndexError:
        print("Error:Index out of range")
my_list=[1,2,3,4,5]
index=int(input("Enter index to access:"))
access_list_element(my_list,index)



#file not found error
try:
    file=open("nonw=existentfile.txt","r")
    content=file.read()
    file.close()
except FileNotFoundError:
    print("File not found!")

#key error
