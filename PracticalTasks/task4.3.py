import csv

def get_top_performers(filepath, number_of_top_students=5):
    stud_list = []
    with open(filepath, 'r', newline='') as st_info:
        reader = csv.reader(st_info)
        for row in reader:
            try:
                stud_list.append((row[0], int(row[1]),  float(row[2])))
            except ValueError:
                continue
    sort_mark = sorted(stud_list, key=lambda x:x[2], reverse=True)
    return [i[0] for i in sort_mark][:number_of_top_students]


def sort_student_file(filepath, new_file=r'students_sorted.csv'):
    stud_list = []
    with open(filepath, 'r', newline='') as st_info:
        reader = csv.reader(st_info)
        for row in reader:
            stud_list.append((row[0], row[1],  row[2]))
    stud_list = sorted(stud_list, key=lambda x: x[1], reverse = True)
    with open(new_file, 'w', newline='') as sort_info:
        writer = csv.writer(sort_info)
        writer.writerows(stud_list)


print(get_top_performers(r'data/students.csv'))
print(sort_student_file(r'data/students.csv', r'data/students_sorted.csv'))
