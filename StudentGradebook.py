#Use a dictionary to store names as keys and grades as values.

#Add new students and grades, update grades, or print averages.

grades = {}
def display_grades():
    if not grades:
        print(" No grades recorded.")
    else:
        print("Student Grades:")
        for student, grade in grades.items():
            print(f"{student}: {grade}")
        
def add_or_update_grade():
    student = input("Enter the student's name: ")
    try:
        grade = float(input(f"Enter the grade for {student}: "))
        grades[student] = grade
        print(f'Grade for "{student}" set to {grade}.')
    except ValueError:
        print("Please enter a valid number for the grade.")


def calculate_average():
    if not grades:
        print("No grades to calculate average.")
    else:
        average = sum(grades.values()) / len(grades)
        print(f"The average grade is: {average:.2f}")
    
def main():
    while True:
        print("\nOptions:")
        print("1. View all grades")
        print("2. Add or update a grade")
        print("3. Calculate average grade")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            display_grades()
        elif choice == '2':
            add_or_update_grade()
        elif choice == '3':
            calculate_average()
        elif choice == '4':
            print("Exiting Student Gradebook.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
