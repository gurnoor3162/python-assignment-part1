def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def main():
    print("Grade Tracker")

    num_subjects = int(input("Enter number of subjects: "))

    marks = []
    
    for i in range(num_subjects):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / num_subjects

    grade = calculate_grade(average)

    print("\n--- Result ---")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
