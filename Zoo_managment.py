from abc import ABC ,abstractmethod
class Animal(ABC):
    def __init__(self,name,age,species):
        self.name=name
        self.age=age
        self.species=species
    
    def __str__(self):
        return f"Name {self.name} - age {self.age} with {self.species}"

class Lion(Animal):
    def __init__(self,name,age,species):
        super().__init__(name,age,species)
    

class Elephant(Animal):
    def __init__(self,name,age,species):
        super().__init__(name,age,species)

class Monkey(Animal):
    def __init__(self,name,age,species):
        super().__init__(name,age,species)

class Zoo:
    def __init__(self):
        self.animals=[]
    
    def add_animals(self,animal):
        self.animals.append(animal)
        print(f"Animal {animal.name} has been added..")
    
    def remove_animals(self,animal_name):
        if self.animals:
            for animal in self.animals:
                if animal.name==animal_name:
                    self.animals.remove(animal)
                    print(f"{animal} has been removed from the Animal list..")
        else:
            print("No any animal exists..")
    
    def list_animals(self):
        if self.animals:
            for animal in self.animals:
                print(f"Animal List: {animal.name}")
        else:
            print('No animal name exist in the list..')

if __name__=="__main__":
    animal = Zoo()
    # lion = Animal('lion',17,'Lion')
    # print(lion)
    # print(animal.animals)
    animal.add_animals(Lion('lion',12,'Lion'))
    animal.add_animals(Elephant('elephant',10,'Elephant'))
    animal.add_animals(Monkey('monkey',12,'Monkey'))

    animal.list_animals()