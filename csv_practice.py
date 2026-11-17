import csv
file_path1 = "passing grades.csv"
file_path2 = "failing grades.csv"
grades = []
with open("student_test_scores.csv","r",newline="") as file:
    with open(file_path2,"w",newline="") as failing_file:
        with open(file_path1, "w", newline="") as passing_file:
            falied = csv.writer(failing_file)
            passing = csv.writer(passing_file)
            content = csv.reader(file)
            next(content)
            for grade in content:
                if int(grade[1]) < 70:
                        falied.writerow(grade)
                        print(f"{grade[0]} failed with a score of {grade[1]}")
                else:
                    passing.writerow(grade)
                    print(f"{grade[0]} passed with a score of {grade[1]}")