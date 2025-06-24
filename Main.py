# Function to calculate grade based on average mark
def calculate_grade(mark):
    # If average mark is 90 or above, return A+
    if mark >= 90:
        return 'A+'
    # If average mark is between 80 and 89, return A
    elif mark >= 80:
        return 'A'
    # If average mark is between 70 and 79, return B
    elif mark >= 70:
        return 'B'
    # If average mark is between 60 and 69, return C
    elif mark >= 60:
        return 'C'
    # If average mark is between 50 and 59, return D
    elif mark >= 50:
        return 'D'
    # If average mark is below 50, return F (fail)
    else:
        return 'F'

# Main function to handle grading process
def main():
    students = []  # List to store all student data

    # Get the number of students to grade
    num_students = int(input("Enter number of students: "))

    # Get the number of subjects for each student
    num_subjects = int(input("Enter number of subjects: "))

    subject_names = []  # List to store the names of subjects

    # Get the name of each subject
    for i in range(num_subjects):
        subject = input(f"Enter name of subject {i+1}: ")
        subject_names.append(subject)  # Add the subject to the list

    # Loop through each student
    for _ in range(num_students):
        name = input("\nEnter student name: ")  # Get the student's name
        marks = []  # List to store marks for this student

        # Get marks for each subject
        for subject in subject_names:
            score = float(input(f"Enter marks for {subject}: "))
            marks.append(score)  # Add score to marks list

        total = sum(marks)  # Total marks for the student
        average = total / num_subjects  # Average mark
        grade = calculate_grade(average)  # Get grade using the function

        # Store all student data in a dictionary
        student_data = {
            "name": name,
            "marks": marks,
            "total": total,
            "average": average,
            "grade": grade
        }

        students.append(student_data)  # Add student record to the list

    # Display the final report card for all students
    print("\n📝 Student Report Card")
    print("-" * 60)

    # Print table headers with fixed spacing
    print(f"{'Name':<15}{'Total':<10}{'Average':<10}{'Grade':<10}")
    print("-" * 60)

    # Print each student's record
    for student in students:
        print(f"{student['name']:<15}{student['total']:<10.2f}{student['average']:<10.2f}{student['grade']:<10}")

    print("-" * 60)

# Entry point of the program
if __name__ == "__main__":
    main()
