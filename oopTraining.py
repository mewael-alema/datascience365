class Patient(object):

    status = "Patient" # this is a global variable for all the intances

    def __init__(self, name , age):
        self.name = name
        self.age = age
        self.conditions = []

    def get_details(self):
        print(f'Patient record: {self.name}, {self.age} years.' + 
        f'Current Information: {self.conditions}.')

    def add_info(self, information):
        self.conditions.append(information)

class Infant(Patient):
    def __init__(self, name, age):
        self.vaccinations = []
        super().__init__(name, age)

    def add_vac(self, vaccine):
        self.vaccinations.append(vaccine)

    def get_details(self):
        print(f'Patient record: {self.name}, {self.age} years.' + 
        f'Current Information: {self.conditions}.' + 
        f'Patient has also had {self.vaccinations} administered to them')


steve = Patient('Steven Hughes', 48)
abigail = Patient('Abigail Sandwick', 30)

steve.add_info("Patient diagnosed with Diabetes Type 2")
steve.get_details()
