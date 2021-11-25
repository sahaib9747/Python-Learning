class MyClass:
    def __init__(self, name, dob, nid) -> None:
        # public attributes
        self.name = name
        self.DOB = dob
        self.NID = nid 

        # protected attributes
        self._name = name
        self._DOB = dob 
        self._NID = nid 
        
        # private attributes
        self.__name = name
        self.__DOB = dob 
        self.__NID = nid 

    def getName(self):
        return self.__name

    def getDOB(self):
        return self.__DOB

    def getNID(self):
        return self.__NID 


obj = MyClass('rihan', '17-12-1999', '1234567890')

print(obj.getName())
print(obj.getDOB())
print(obj.getNID())

print(obj.getName())
print(obj.getDOB())
print(obj.getNID())

print(obj.getName())
print(obj.getDOB())
print(obj.getNID())


