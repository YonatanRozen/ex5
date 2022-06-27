import json
import os
import string


def names_of_registered_students(input_json_path, course_name):
    # Opening JSON file
    file = open(input_json_path)

    registered_students = []

    # Parsing the data from the JSON file
    # Returns a dictionary
    data = json.load(file)

    for name, courses in zip(data["student_name"], data["registered_courses"]):
        if course_name in courses:
            registered_students.append(name)

    file.close()
    return registered_students


def enrollment_numbers(input_json_path, output_file_path):
    # Opening JSON file
    file = open(input_json_path)

    # Parsing the data from the JSON file
    # Returns a dictionary
    data = json.load(file)

    courses_dict = get_dict_of_courses(data)
    for student_courses in data["registered_courses"]:
        update_enrollment_numbers(student_courses, courses_dict)

    key_list = list(courses_dict.keys())
    val_list = list(courses_dict.values())
    for course_data in courses_dict:
        pos = val_list.index(course_data)
        json.dump(key_list[pos] + ' ' + course_data + '\n', output_file_path, indent=4)
    file.close()


def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    pass


def update_enrollment_numbers(registered_courses, courses_dict):
    for course in registered_courses:
        courses_dict[course] += 1


def get_dict_of_courses(data):
    course_list = []
    for courses in data["registered_courses"]:
        for item in courses:
            if item not in course_list:
                course_list.append(item)
    course_list.sort()

    course_dict = {}
    for item in course_list:
        course_dict[item] = 0
    return course_dict
