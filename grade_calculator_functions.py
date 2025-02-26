def get_student_score():
    """Prompt the user for a valid score and return it."""
    try:
        score = float(input("Enter your score: "))
        if 0 <= score <= 100:
            return score
        else:
            print("Error: Score must be between 0 and 100.")
            return None 
  except ValueError:
        print("Error: Invalid input. Please enter a number.")
        return None


def calculate_grade(score):
    """Return a letter grade based on the given score."""
    if score is None:
        return "Invalid"
    elif score >= 90:
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
    if score is not None:
        grade = calculate_grade(score)
        print(f"Your grade is: {grade}")
