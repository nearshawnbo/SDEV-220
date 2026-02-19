# Superclass Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Subclass Automobile
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")  # Vehicle type is always "car"
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print(f"\nVehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

# Function to get user input safely
def get_user_input():
    year = input("Enter the year of the car: ").strip()
    make = input("Enter the make of the car: ").strip()
    model = input("Enter the model of the car: ").strip()
    
    # Validate doors input
    while True:
        doors = input("Enter the number of doors (2 or 4): ").strip()
        if doors in ["2", "4"]:
            doors = int(doors)
            break
        else:
            print("Invalid input. Please enter 2 or 4.")

    # Validate roof input
    while True:
        roof = input("Enter the type of roof (solid or sun roof): ").strip().lower()
        if roof in ["solid", "sun roof"]:
            break
        else:
            print("Invalid input. Please enter 'solid' or 'sun roof'.")
    
    return year, make, model, doors, roof

# Main program
def main():
    print("Welcome! Let's enter information about your car.")
    year, make, model, doors, roof = get_user_input()
    
    my_car = Automobile(year, make, model, doors, roof)
    my_car.display_info()

if __name__ == "__main__":
    main()
