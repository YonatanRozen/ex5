import json
import os
import string


def names_of_registered_students(input_json_path, course_name):
    # Opening JSON file
    file = open(input_json_path)

    # Parsing data
    data = json.load(file)
    key_list = list(data.keys())

    # Creating list of names...
    course_list = []
    for key in key_list:
        if course_name in data[key]["registered_courses"]:
            course_list.append(data[key]["student_name"])
        else:
            continue

    file.close()
    return course_list


def enrollment_numbers(input_json_path, output_file_path):
    # Opening JSON file
    in_file = open(input_json_path, 'r')
    out_file = open(output_file_path, 'w')

    # Parsing data
    data = json.load(in_file)
    keys_json = list(data.keys())

    dic = get_student_course_dict(input_json_path, data, keys_json)
    keys_courses = sorted(list(dic.keys()))
    for key in keys_courses:
        out_file.write('"{}" {}{}'.format(key, dic[key], '\n'))

    in_file.close()
    out_file.close()


def courses_for_lecturers(json_directory_path, output_json_path):
    files = os.listdir(json_directory_path)
    dict_lecturers = {}
    for file in files:
        if file.endswith(".json"):
            current_file = open(json_directory_path + "\\" + file, "r")
            data = json.load(current_file)
            for course in data:
                for lecturer in data[course]["lecturers"]:
                    if lecturer in dict_lecturers:
                        if data[course]["course_name"] not in dict_lecturers[lecturer]:
                            dict_lecturers[lecturer].append(data[course]["course_name"])
                    else:
                        dict_lecturers[lecturer] = [data[course]["course_name"]]
            current_file.close()
    output_file = open(output_json_path, "w")
    json.dump(dict_lecturers, output_file, indent=4)
    output_file.close()


def get_all_lecturers(data):
    lecturers = {}
    keys = list(data.keys())
    for key in keys:
        for lecturer in data[key]['lecturers']:
            if lecturer not in lecturers:
                lecturers[lecturer] = []
            else:
                continue
    return lecturers


def get_lecturer_course_list(data, lecturer):
    courses = []
    keys = list(data.keys())
    for key in keys:
        if lecturer in data[key]['lecturers'] and data[key]['course_name'] not in courses:
            courses.append(data[key]['course_name'])
    return courses


def get_student_course_dict(json_file_path, data, keys):
    dic = {}
    for key in keys:
        for item in data[key]["registered_courses"]:
            if item not in dic:
                students_registered = names_of_registered_students(json_file_path, item)
                amount = len(students_registered)
                dic[item] = amount
            else:
                continue
    return dic


def get_json_files(json_directory_path):
    files = []
    for file in os.listdir(json_directory_path):
        if file.endswith('.json'):
            files.append(json_directory_path + "\\" + file)
        else:
            continue
    return files
