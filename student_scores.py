# Get the number of students
n = int(input("Enter the number of students: "))

# Initialize the student_scores dictionary
student_scores = {}

# Collect student scores
for i in range(n):
    a = input("Enter student name and scores: ")  # Read input for each student
    b = a.split()  # Split input into a list
    name = b[0]  # The first element is the student's name
    scores = list(map(float, b[1:]))  # The remaining elements are the scores
    student_scores[name] = scores  # Store the scores in the dictionary

# Get the student name for which the average needs to be calculated
query = input("Enter student name to query average score: ")

# Calculate the average score for the queried student
avg = sum(student_scores[query]) / len(student_scores[query])

# Print the average score
print(f"The average score for {query} is: {avg:.2f}")
