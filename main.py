import os
def translateLetter(*letters):
    letter_points = {'A+': 4.3, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
                     'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'D-': 0.7}

    return [letter_points[letter] for letter in letters]

def translatePercentage(*percentages):
    percentage_points = {range(95, 101): 4.3, range(90, 95): 4.0, range(85, 90): 3.7, range(80, 85): 3.3,
                         range(75, 80): 3.0, range(70, 75): 2.7, range(65, 70): 2.3, range(60, 65): 2.0,
                         range(55, 60): 1.7, range(50, 55): 1.3, range(45, 50): 1.0, range(40, 45): 0.7}

    points = []
    for percentage in percentages:
        for score_range, point in percentage_points.items():
            if percentage in score_range:
                points.append(point)
                break

    return points

def calculateGPA(*args):
    points = args[::2]
    credits = args[1::2]

    total_weighted_points = sum(p * c for p, c in zip(points, credits))
    total_credits = sum(credits)

    gpa = 0.0

    if total_credits != 0:
        gpa = total_weighted_points / total_credits

    return round(gpa, 2)


num_courses = int(input("Write number of courses: "))
courses = []

for i in range(num_courses):
    course_name = input(f"Write name of course {i + 1}: ")
    score_input = input(f"Write score for course {i + 1} (letter or percentage): ")
    credits = float(input(f"Write number of credits course {i + 1}: "))

    if '%' in score_input:
        scores = translatePercentage(int(score_input.rstrip('%')))
    else:
        scores = translateLetter(score_input)

    courses.extend(scores)
    courses.append(credits)

overall_gpa = calculateGPA(*courses)
print(f"\nOverall GPA: {overall_gpa}")



def process_course_file(course_file_path, credits):
    with open(course_file_path, 'r') as file:
        lines = file.readlines()

    scores = [line.strip() for line in lines]
    if '%' in scores[0]:
        points = translatePercentage(*map(int, scores))
    else:
        points = translateLetter(*scores)

    return calculateGPA(*points, *credits)

directory_path = "grades"

credits_file_path = os.path.join(directory_path, "credits.txt")
with open(credits_file_path, 'w') as credits_file:
    credits_values = [float(line.strip()) for line in credits_file]

overall_gpas = []
for file_name in os.listdir(directory_path):
    if file_name.endswith(".txt") and file_name != "credits.txt":
        course_file_path = os.path.join(directory_path, file_name)
        gpa = process_course_file(course_file_path, credits_values)
        overall_gpas.append((file_name.split('.')[0], gpa))

output_file_path = os.path.join(directory_path, "overallGPAs.txt")
with open(output_file_path, 'w') as output_file:
    for course, gpa in overall_gpas:
        output_file.write(f"{course}: {gpa}\n")

class Student:
    def __init__(self, name, number_courses):
        self.name = name
        self.number_courses = number_courses
        self.scores = {}
        self.gpa = 0.0
        self.status = ""

    def setName(self, new_name):
        if isinstance(new_name, str):
            self.name = new_name
            return True
        return False

    def setNumberCourses(self, new_value):
        if isinstance(new_value, int) and new_value > 0:
            self.number_courses = new_value
            return True
        return False

    def registerScores(self, course_name, course_score, course_credits):
        if course_name not in self.scores and isinstance(course_score, (int, float)) and isinstance(course_credits, (int, float)):
            self.scores[course_name] = {'score': course_score, 'credits': course_credits}
            return True
        return False

    def calculateGPA(self):
        total_weighted_points = 0
        total_credits = 0

        for course, info in self.scores.items():
            total_weighted_points += info['score'] * info['credits']
            total_credits += info['credits']

        if total_credits != 0:
            self.gpa = round(total_weighted_points / total_credits, 2)
        else:
            self.gpa = 0.0

    def setStatus(self):
        self.calculateGPA()
        if self.gpa >= 1.0:
            self.status = "Passed"
        else:
            self.status = "Not Passed"

    def showGPA(self):
        self.calculateGPA()
        print(f"{self.name}'s GPA: {self.gpa}")

    def showStatus(self):
        self.setStatus()
        print(f"{self.name}'s Status: {self.status}")

    def showScores(self):
        print(f"{self.name}'s Scores:")
        for course, info in self.scores.items():
            print(f"{course}: Score - {info['score']}, Credits - {info['credits']}")


student1 = Student("John Doe", 3)
student1.registerScores('Math', 4.3, 4)
student1.registerScores('Chemistry', 3.3, 3)
student1.registerScores('English', 4.0, 4)

student1.showScores()
student1.showGPA()
student1.showStatus()



























