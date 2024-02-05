class person(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def Display(self):
        print(self.name, self.id)

emp = person("SAtyam", 102)
emp.Display()

class Emp(person):
    def print(self):
        print("Emp class called")
Emp_details = Emp("Mayank", 103)

Emp_details.Display()
Emp_details.print()
