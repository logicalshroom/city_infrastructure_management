# Vehicle Registratation System

class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.vehicle_type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

    def display_details(self):
        print(f"Registration: {self.registration_number}, Type: {self.vehicle_type}, Owner: {self.owner}")

# Demo a script using the expected outcome

vehicles = {}

def register_vehicle(reg_num, vehicle_type, owner):
    if reg_num in vehicles:
        print("Error: Registration Number already exists.")
        return
    vehicles[reg_num] = Vehicle(reg_num, vehicle_type, owner)
    print(f"Vehicle Registration Number: {reg_num} successfully registered!")

def update_vehicle_owner(reg_num, new_owner):
    if reg_num in vehicles:
        vehicles[reg_num].update_owner(new_owner)
        print(f"Vehicle Owner for Registration Number {reg_num} changed to {new_owner}.")
    else:
        print(f"Vehicle not found.")

def display_all_vehicles():
    for vehicle in vehicles.values():
        vehicle.display_details()

# build the CLI

print(f"Welcome to the Vehicle Management System!")

while True:
        command = input("Please input your command:\n (register, update, display, exit)\n >>>").lower()
        if command == "exit":
            break

        try:
            if command == "register":
                reg_num = input(f"Please enter the Registration Number: ")
                vehicle_type = input(f"Please enter the Vehicle Type: ")
                owner = input(f"Please enter the Owner's Name: ")
                register_vehicle(reg_num, vehicle_type, owner)
            elif command == "update":
                reg_num = input(f"Please enter the Registration Number: ")
                new_owner = input(f"Please enter the new Owner's Name: ")
                update_vehicle_owner(reg_num, new_owner)
            elif command == "display":
                display_all_vehicles()
        except Exception as e:
            print(f"Error Occurred: {e}")

print(f"Goodbye!")

