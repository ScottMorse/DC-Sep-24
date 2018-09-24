
class Person:

    people = []
    
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.people_greeted = []
        Person.people.append(self)
        self.greetings = 0
    
    def greet(self, other_person):
        print(f"Hello {other_person.name}, I am {self.name}.")
        self.greetings += 1
        if other_person not in self.people_greeted:
            self.people_greeted.append(other_person)
    
    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name}'s phone #: {self.phone}")

    def add_friend(self,other_person):
        self.friends.append(other_person)

    @property
    def num_friends(self):
        return len(self.friends)
    
    @property
    def unique_greets(self):
        return len(self.people_greeted)
    
    def __repr__(self):
        return f"<{self.name} {self.email} {self.phone}>"


sonny = Person('Sonny','sonny@hotmail.com', '483-485-4948')

jordan = Person('Jordan','jordan@aol.com', '495-586-3456')

[prs.print_contact_info() for prs in Person.people]

sonny.add_friend(jordan)
jordan.add_friend(sonny)

class Vehicle:

    def __init__(self,make,model,year):

        self._make = make
        self._model = model
        self._year = year
    
    @property
    def make(self):
        return self._make

    @property
    def mmodel(self):
        return self._model
    
    @property
    def year(self):
        return self._year

    def print_info(self):
        print(f"{self.year} {self.make} {self.year}")

