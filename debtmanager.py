import json

LIST_CHOICE = ["1. Recap","2. Add person", "3. Add debt", "0. Exit"]
FILENAME = "debt.json"

class Person:
    def __init__(self, name, debt=0):
        self.name = name
        self.debt = debt

class Program:
    def __init__(self):
        self.running = True
        self.people:list[Person] = []
        
    
    def save_people(self):
        with open(FILENAME, "w") as file:
            json.dump([person.to_dict() for person in self.people], file)

    def load_people(self):
        with open(FILENAME, "r") as file:
            people_list = json.load(file)
            self.people = [Person(person['name'], person['debt']) for person in people_list]
    
    def recap(self):
        print("\n========== RECAP ==========\n")
        if len(self.people) == 0:
            print("No person added.")
        else:
            for person in self.people:
                print(f"{person.name}: {person.debt}")
        print("\n===========================\n")
    
    def add_person(self):
        print("\n========== ADD PERSON ==========\n")
        person = input("Enter the name of the person : ")
        
        # regex letters person
        
        debt = input("Enter the initial debt (0 if none) : ")
        
        # regex number debt
        
        if debt=="":
            debt = 0
        debt = float(debt)

        self.people.append(Person(person, debt))

        print(f"{person} added successfully !")
        print("\n===========================\n")
    
    def add_debt(self):
        print("\n========== ADD DEBT ==========\n")
        name = input("Enter the name of the person whose debt you want to add : ")
        
        # regex letters person
        
        debt = input("Enter the amount of debt to add \nPositive : this person owes you money\nNegative: you owe him/her money\n\n=>")
        
        # regex number debt
        
        if debt=="":
            debt = 0
        debt = float(debt)
        
        for person in self.people:
            if person.name == name:
                person.debt += debt
                print(f"{name}'s debt has been updated successfully !")
                print(f"New debt: {person.debt}")
                print("\n===========================\n")
                break
            else:
                print(f"{name} not found.")
                print("\n===========================\n")
    
    def main(self):
        print("Loading data...")
        self.load_people()
        print("Data loaded successfully !")
        print("\n========== MAIN MENU ==========\n")
        while self.running:
            for elt in LIST_CHOICE:
                print(f"{elt}")
            print("\n===========================\n")
            try:
                choice = int(input("=> "))
            except:
                print("Invalid input. Please try again.")
                continue

            if choice in range(0,len(LIST_CHOICE)):
                if choice == 1:
                    self.recap()
                elif choice == 2:
                    self.add_person()
                elif choice == 3:
                    self.add_debt()
                else:
                    print("Saving data...")
                    self.save_people()
                    print("Data saved successfully !")
                    self.running = False
                    print("Exiting the program.")
                    break

Program().main()