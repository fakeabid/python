python = {'abin', 'hadi', 'aswin', 'john', 'arjun'}
data_sc = {'john', 'arjun', 'aswin', 'amal'}

python.add('abid')
data_sc.pop()

both = python.intersection(data_sc)
print(both)

only_python = python - data_sc
print(only_python)

all_students = python | data_sc
print(all_students)

courses = {
    'python': len(python),
    'data_sc': len(data_sc)
}

for name, stds in courses.items():
    print(f'Course: {name}, Students: {stds}')

courses_2026 = {key:val*2 for key,val in courses.items()}
print(courses_2026)