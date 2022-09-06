class Student:
    def __init__(self, name, age, id):
        if type(name) != str:
            raise TypeError("Name should be a string.")
        if type(age) != int:
            raise TypeError("Age should be an int.")
        if type(id) != int:
            raise TypeError("ID should be an int.")
        if age < 0:
            raise TypeError("Age should not be negative")
        if id < 0:
            raise TypeError("ID should not be negative")
        self._name = name
        self._age = age
        self._id = id
    
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
