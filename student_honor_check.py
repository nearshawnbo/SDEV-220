# Author: Your Name
# File Name: student_honor_check.py
# Description: This program accepts student names and GPAs, then determines
#              if the student qualifies for the Dean's List or the Honor Roll.
#              Processing stops when the last name 'ZZZ' is entered.

def main():
    while True:
        # Ask for last name
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ").strip()
        if last_name.upper() == 'ZZZ':
            print("Exiting program. Goodbye!")
            break
        
        # Ask for first name
        first_name = input("Enter the student's first name: ").strip()
        
        # Ask for GPA and ensure it's a float
        try:
            gpa = float(input("Enter the student's GPA: "))
        except ValueError:
            print("Invalid input. GPA must be a number. Try again.")
            continue
        
        # Check for Dean's List
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!")
        # Check for Honor Roll (note: GPA >= 3.5 also qualifies for Honor Roll)
        if gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll!")
        
        print("-" * 40)

# Run the program
if __name__ == "__main__":
    main()
