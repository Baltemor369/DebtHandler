import json
from Person import Person
from const import *

class Program:
    def __init__(self):
        self.running = True
        self.people:list[Person] = []

    def list_names(self):
        ls = []
        for person in self.people:
            ls.append(person.name)
        return ls
            
    
    def save_people(self):
        with open(FILENAME, "w") as file:
            json.dump([person.to_dict() for person in self.people], file)

    def load_people(self):
        try:
            with open(FILENAME, "r") as file:
                people_list = json.load(file)
                self.people = [Person(person['name'], person['debt']) for person in people_list]
        except FileNotFoundError:
            print(f"No previous data found in {FILENAME}. Starting with an empty list.")
            with open(FILENAME, "w") as file:
                json.dump([], file)
    
    def menu_recap(self):
        print("\n========== RECAP ==========\n")
        if len(self.people) == 0:
            print("No person added.")
        else:
            for person in self.people:
                print(f"{person.name}: {person.debt}")
        print("\n===========================\n")
    
    def menu_add_person(self):
        print("\n========== ADD PERSON ==========\n")
        run = False
        while not run:
            person = input("Enter the name of the person(or 'exit' to leave) : ")
            
            # regex letters person

            if person == "exit":
                break
            
            debt = input("Enter the initial debt (0 if none) : ")
            
            # regex number debt
            
            run = self.add_person(person.capitalize(), debt)
        print("\n===========================\n")
    
    def add_person(self, name:str, amount:str):
        if name in self.list_names():
            print(f"{name} already exists in the list.")
            return False
        
        if not name:
            print("Invalid input. Please enter a non-empty name.")
            return False

        if not amount:
            amount = 0
        
        try:
            amount = float(amount)
        except:
            print("Invalid input. Please enter a valid number.")
            return False

        self.people.append(Person(name.capitalize(), amount))
        print(f"{name} added successfully !")
        return True


    def menu_add_debt(self):
        print("\n========== ADD DEBT ==========\n")
        run = False
        while not run:
            name = input("Enter the name of the person whose debt you want to add(or 'exit' to leave) : ")
            
            # regex letters person

            if name == "exit":
                break
            
            debt = input("Enter the amount of debt to add \nPositive : this person owes you money\nNegative: you owe him/her money\n\n=>")
            
            # regex number debt
            
            run = self.add_debt(name.capitalize(), debt)
        print("\n===========================\n")

    def add_debt(self, name:str, amount:str): 
        if not name in self.list_names():
            print(f"{name} not in the list.")
            c = input("Do you want to add {name} ?(y/n)")
            if c.lower() in ['y', 'yes']:
                self.add_person(name,0)
            else:
                return False
        
        if not amount:
            amount = 0
        
        try:
            amount = float(amount)
        except:
            print("Invalid input. Please enter a valid number.")
            return False

        for person in self.people:
            if person.name == name:
                person.debt += amount
                print(f"{name}'s debt has been updated successfully !")
                print(f"New debt: {person.debt}")
                return True
    
    def menu_main(self):
        print("Loading data...")
        self.load_people()
        print("Data loaded successfully !")

        print("\n========== MAIN MENU ==========\n")
        while self.running:
            # display choice menu
            for elt in LIST_CHOICE:
                print(f"{elt}")
            print("\n===========================\n")

            # get user inputs
            try:
                choice = int(input("=> "))
            except:
                print("Invalid input. Please try again.")
                continue
            
            # check input is in the list
            if choice in range(0,len(LIST_CHOICE)):
                if choice == 1:
                    self.menu_recap()
                elif choice == 2:
                    self.menu_add_person()
                elif choice == 3:
                    self.menu_add_debt()
                else:
                    print("Saving data...")
                    self.save_people()
                    print("Data saved successfully !")
                    
                    self.running = False
                    print("Exiting the program.")
                    break