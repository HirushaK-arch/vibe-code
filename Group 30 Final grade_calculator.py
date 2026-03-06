def main():
    # Ask for student's name
    name = input("Enter the student's name: ")

    # Ask for 3 subject marks
    try:
        mark1 = float(input("Enter mark for Subject 1: "))
        mark2 = float(input("Enter mark for Subject 2: "))
        mark3 = float(input("Enter mark for Subject 3: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for marks.")
        return

    # Calculate the average
    average = (mark1 + mark2 + mark3) / 3

    # Determine Grade
    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"

    # Display results
    print("-" * 30)
    print(f"Name    : {name}")
    print(f"Average : {average:.1f}")
    print(f"Grade   : {grade}")
    print("-" * 30)

if __name__ == "__main__":
    main()
