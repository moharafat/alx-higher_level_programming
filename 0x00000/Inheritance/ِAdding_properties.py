class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def display(self):
    print(self.name, self.age)
class Student(Person):
  def __init__(self, name, age, dob):
    self.sName = name
    self.sAge = age
    self.dob = dob  
    super().__init__("rahul", age)
  def displayInfo(self):
    print(self.sName, self.sAge, self.dob)
obj = Student("Mayabnk", 23, "16-03-2000")
obj.display
obj.displayInfo()