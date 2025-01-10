# Step 1: Input student name
student_name = input("Enter the student's name: ")

# Step 2: Input number of subjects (with validation)
while True:
    try:
        num_subjects = int(input("How many subjects? "))
        if num_subjects <= 0:
            print("The number of subjects must be greater than 0. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Step 3: Input scores for each subject (with validation)
scores = []
for i in range(num_subjects):
    while True:
        try:
            score = float(input(f"Enter score for subject {i+1}: "))
            if score < 0 or score > 100:
                print("Score must be between 0 and 100. Please try again.")
            else:
                scores.append(score)
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Step 4: Calculate the average score
average_score = sum(scores) / len(scores)

# Step 5: Determine the grade
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

# Step 6: Display the final output
print("\n--- Student Report ---")
print(f"Name: {student_name}")
print(f"Average Score: {average_score:.2f}")
print(f"Grade: {grade}")