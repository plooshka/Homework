import csv
from operator import itemgetter


def get_top_performers(file_path: str, number_of_top_students=5) -> list:
    """The function which receives file path and returns names of top performer students"""

    file = open(file_path, "r")
    file_reader = csv.DictReader(file, delimiter=",")
    sorted_list_by_avg = sorted(file_reader,
                                key=itemgetter('average mark'),
                                reverse=True,
                                )
    names_of_top_students = list()
    for student in sorted_list_by_avg[0:number_of_top_students]:
        names_of_top_students.append(student['student name'])
    return names_of_top_students


def sort_student_by_age(file_path: str) -> str:
    """The function which receives the file path with students info and
    writes CSV student information to the new file in descending order of age
    """

    file = open(file_path, "r")
    file_reader = csv.DictReader(file, delimiter=",")
    sorted_list_by_age = sorted(file_reader,
                                key=itemgetter('age'),
                                reverse=True,
                                )
    file.close()
    file = open("desc_age_students.csv", "w")
    file_writer = csv.writer(file, delimiter=",", lineterminator="\r")
    file_writer.writerow(["student name", "age", "average mark"])
    for student in sorted_list_by_age:
        file_writer.writerow([student['student name'],
                              student['age'],
                              student["average mark"],
                              ])
    return "File was created!"


print(get_top_performers("students.csv"))
print(sort_student_by_age("students.csv"))
