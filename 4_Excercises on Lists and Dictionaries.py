eren = {
 "name": "Eren",
 "homework": [90.0,97.0,75.0,92.0],
 "quizzes": [88.0,40.0,94.0],
 "tests": [75.0,90.0]
}
mikasa = {
"name": "Mikasa",
"homework": [100.0, 92.0, 98.0, 100.0],
"quizzes": [82.0, 83.0, 91.0],
"tests": [89.0, 97.0]
}
armin = {
"name": "Armin",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}
students =  [eren,mikasa,armin]
print(students[0])
print(students[1])
print(students[2])

def average(numbers):
    total = sum(numbers)
    total = float(total)
    total = total /len(numbers)
    return total
def get_average(student):
    homework = (average(student["homework"]))* 0.1
    quizzes = (average(student["quizzes"])) * 0.3
    tests = (average(student["tests"]))* 0.6
    score = homework + quizzes + tests
    return score
def get_letter_grade(score):
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
    
score = get_average(eren)
print(score)
print(get_letter_grade(score))

score1 = get_average(mikasa)
print(score1)
print(get_letter_grade(score1))

score2 = get_average(armin)
print(score2)
print(get_letter_grade(score2))

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)
class_average = get_class_average(students)
print(class_average)
print(get_letter_grade(class_average))