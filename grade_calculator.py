# grade_calculator.py

def calculate_average(marks):
    if not marks:
        raise ValueError("Marks list cannot be empty")
    return sum(marks) / len(marks)

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def is_pass(average):
    return average >60


if __name__ == "__main__":
    sample_marks = [85, 90, 78]
    avg = calculate_average(sample_marks)
    print("Marks:", sample_marks)
    print("Average:", avg)
    print("Grade:", get_grade(avg))
    print("Pass:", is_pass(avg))
