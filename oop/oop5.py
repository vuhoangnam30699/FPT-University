from abc import ABC, abstractmethod

# -------------------------------------------------------------------------
# 1. Organism (Abstract Class)
# -------------------------------------------------------------------------
class Organism(ABC):
    def __init__(self, id_organism, name, habitat):
        self.__id = id_organism
        self.__name = name
        self.__habitat = habitat

    def id(self):
        return self.__id
    
    def id(self, value):
        self.__id = value

    def name(self):
        return self.__name
    
    def name(self, value):
        self.__name = value

    def habitat(self):
        return self.__habitat
    
    def habitat(self, value):
        self.__habitat = value

    def displayInfo(self):
        print(f"ID={self.__id}, Name={self.__name}, Habitat={self.__habitat}", end="")

    @abstractmethod
    def getDescription(self):
        pass


# -------------------------------------------------------------------------
# 2. Animal Class
# -------------------------------------------------------------------------
class Animal(Organism):
    def __init__(self, id_organism, name, habitat, species, speed):
        super().__init__(id_organism, name, habitat)
        self.__species = species
        self.__speed = speed

    def species(self):
        return self.__species

    def speed(self):
        return self.__speed

    def move(self):
        pass

    def getDescription(self):
        return f", Species={self.__species}, Speed={self.__speed}"


# -------------------------------------------------------------------------
# 3. Plant Class
# -------------------------------------------------------------------------
class Plant(Organism):
    def __init__(self, id_organism, name, habitat, plantType, height):
        super().__init__(id_organism, name, habitat)
        self.__plantType = plantType
        self.__height = height

    def plantType(self):
        return self.__plantType

    def height(self):
        return self.__height

    def grow(self):
        pass

    def getDescription(self):
        return f", PlantType={self.__plantType}, Height={self.__height}"


# -------------------------------------------------------------------------
# 4. ForestManager Class
# -------------------------------------------------------------------------
class ForestManager:
    def __init__(self):
        self.organisms = []

    def addAnimal(self, animal):
        self.organisms.append(animal)

    def addPlant(self, plant):
        self.organisms.append(plant)

    def displayAll(self):
        for org in self.organisms:
            org.displayInfo()
            print(org.getDescription())

    def searchById(self, id_organism):
        for org in self.organisms:
            if org.id == id_organism:
                org.displayInfo()
                print(org.getDescription())
                return
        print("Not found")

    def deleteById(self, id_organism):
        for org in self.organisms:
            if org.id == id_organism:
                self.organisms.remove(org)
                return
        print("Not found")

    def countOrganisms(self):
        animals_count = sum(1 for org in self.organisms if isinstance(org, Animal))
        plants_count = sum(1 for org in self.organisms if isinstance(org, Plant))
        print(f"Animals: {animals_count}")
        print(f"Plants: {plants_count}")

    def displayAnimalsOnly(self):
        for org in self.organisms:
            if isinstance(org, Animal):
                org.displayInfo()
                print(org.getDescription())

    def displayPlantsOnly(self):
        for org in self.organisms:
            if isinstance(org, Plant):
                org.displayInfo()
                print(org.getDescription())


# -------------------------------------------------------------------------
# 5. Main Menu Program
# -------------------------------------------------------------------------
manager = ForestManager()

manager.addAnimal(Animal("A01", "Tiger", "Forest", "Mammal", 60))
manager.addPlant(Plant("P01", "Rose", "Garden", "Flower", 1.2))

while True:
    print("\n1. Add Animal")
    print("2. Add Plant")
    print("3. Display all")
    print("4. Search by ID")
    print("5. Delete by ID")
    print("6. Count Animal & Plant")
    print("7. Display Animals")
    print("8. Display Plants")
    print("0. Exit")
        
    choice = input().strip()

    if choice == "1":
        id_org = input().strip()
        name = input().strip()
        habitat = input().strip()
        species = input().strip()
        speed = float(input().strip())
        manager.addAnimal(Animal(id_org, name, habitat, species, speed))

    elif choice == "2":
        id_org = input().strip()
        name = input().strip()
        habitat = input().strip()
        plant_type = input().strip()
        height = float(input().strip())
        manager.addPlant(Plant(id_org, name, habitat, plant_type, height))

    elif choice == "3":
        manager.displayAll()

    elif choice == "4":
        id_org = input().strip()
        manager.searchById(id_org)

    elif choice == "5":
        id_org = input().strip()
        manager.deleteById(id_org)

    elif choice == "6":
        manager.countOrganisms()

    elif choice == "7":
        manager.displayAnimalsOnly()

    elif choice == "8":
        manager.displayPlantsOnly()

    elif choice == "0":
        break