def get_student_score():
    """Prompts the user for a valid score between 0 and 100."""
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid input. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_grade(score):
    """Determines the letter grade based on the score."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

if __name__ == "__main__":
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your grade is: {grade}")
