students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]

def validat_score(score):
    return isinstance(score, (int,float)) and 0 <= score <= 100

def calculate_grade(score):
    if not validat_score(score):
       return f"Invalid score: {score}. Must between 0 and 100"
    if score >= 90: 
       return "A"
    elif score >= 80:
       return "B"
    elif score >= 70:
       return "C"
    elif score >= 60:
       return "D"
    else:
       return "F"

def calculate_average(students):
    total = 0
    for student in students:
       total = total + student["score"]
    average_score = total / len(students)
    return average_score


def find_highest_and_lowest(students):
    sorted_students = sorted(students, key=lambda item: item['score'])
    lowest = sorted_students[0]
    highest = sorted_students[-1]
    return lowest, highest

def count_pass_fail(students):
    fail = []
    passed = []
    for student in students:
        if student["score"] > 50:
           passed.append(student)
        else:
           fail.append(student) 
    failed_student = len(fail)
    passed_student = len(passed)
    return failed_student, passed_student

def student_score_above_average(students):
    average_score = calculate_average(students)
    return [s for s in students if s["score"] > average_score]

def generate_report(students, passing_score=50):
    """Generate and print a summary report for the class."""
    print("=== CLASS EXAM RESULTS REPORT ===")
    print(f"Total Students: {len(students)}")
    
    avg_score = calculate_average(students)
    print(f"Class Average Score: {avg_score:.2f}")
    
    highest, lowest = find_highest_and_lowest(students)
    if highest and lowest:
        print(f"Highest Score: {highest['name']} ({highest['score']})")
        print(f"Lowest Score: {lowest['name']} ({lowest['score']})")
    
    passed, failed = count_pass_fail(students)
    print(f"Passed: {passed} | Failed: {failed}")
    
    print("\n--- Individual Breakdown ---")
    for s in students:
        grade = calculate_grade(s["score"])
        status = "PASSED" if s["score"] >= passing_score else "FAILED"
        print(f"Name: {s['name']} | Score: {s['score']} | Grade: {grade} | Status: {status}")
    
    above_avg = student_score_above_average(students)
    print("\n--- Students Above Class Average ---")
    for s in above_avg:
        print(f"- {s['name']} ({s['score']})")
generate_report(students)