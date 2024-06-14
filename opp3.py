#access modify

class Super:
    #public data member
    var1=None
    #protected data member
    _var2=None
    #private data member
    __var3=None

    #constructor
    def __init__(self,var1,var2,var3):
        self.var1=var1
        self._var2=var2
        self.__var3=var3

    #public member function
    def displayPublicMembers(self):
        #accesing public data member
        print("public member:",self.var1)

    #protected member function
    def _displayProtectedMembers(self):
        #accesing protected data member
        print("protected member:",self._var2)

    #private member function
    def __displayPrivateMembers(self):
        #accesing private data member
        print("private member:",self.__var3)

    #public member function
    def accessPrivateMembers(self):
        #accesing private data member
        self.__displayPrivateMembers()

#derived class
class Sub(Super):
    #constructor
    def __init__(self,var1,var2,var3):
        #calling constructor of super class
        Super.__init__(self,var1,var2,var3)
        
    #public member function
    def accessProtectedMembers(self):
        #accesing protected data member of super class
        self._displayProtectedMembers()

obj=Sub("Hello","all","people !")
#calling public member function of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

#object can access protected members
print("object can access protected members",obj._var2)

#object can not access private members, so it will generate attributes
#print(obj.__var3)