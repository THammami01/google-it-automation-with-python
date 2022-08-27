#!/usr/bin/env python3
import csv


csv.register_dialect('empDialect', skipinitialspace=True, strict=True)


def read_employees(csv_file_location):
        employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')

        employee_list = []
        for data in employee_file:
                employee_list.append(data)

        return employee_list


def process_data(employee_list):
        department_list = []
        for employee_data in employee_list:
                department_list.append(employee_data['Department'])

        department_data = {}
        for department_name in set(department_list):
                department_data[department_name] = department_list.count(department_name)

        return department_data


def write_report(dictionary, report_file):
        with open(report_file, "w+") as f:
                for k in sorted(dictionary):
                        f.write(str(k)+':'+str(dictionary[k])+'\n')
                f.close()


USERNAME = "student-02-10a7082c8f08"
employee_list = read_employees("/home/{}/data/employees.csv".format(USERNAME))
dictionary = process_data(employee_list)
write_report(dictionary, '/home/{}/test_report.txt'.format(USERNAME))
