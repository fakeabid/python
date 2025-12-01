# You are managing an online course portal that keeps track of student enrollments in two subjects: "Frontend" and "Backend".
# Create two sets:
# One with the names of students enrolled in the Frontend course
# One with the names of students enrolled in the Backend course
# Perform the following tasks:
# Add a new student to the Backend course
# Remove a student from the Frontend course
# Display the list of students who are enrolled in both courses
# Display the list of students who are enrolled only in Backend, but not in Frontend
# Display the total number of unique students
# Create a dictionary where:
# Keys are course names ("Frontend", "Backend")
# Values are the number of students enrolled in each
# Print each course name with the number of students using a loop
# Using dictionary comprehension, create a new dictionary that adds a "Fullstack" course by combining student counts from both existing courses.

frontend = {'abin', 'hadi', 'aswin', 'john', 'arjun'}
backend = {'john', 'arjun', 'aswin', 'amal'}

backend.add('abid')
frontend.pop()

print(frontend & backend)
print(backend - frontend)
print(len(frontend | backend))

courses = {
    'frontend':len(frontend),
    'backend': len(backend)
}

for name, stds in courses.items():
    print(f'Course: {name}, Students: {stds}')

courses_updated = {name: stds for name, stds in courses.items()}
courses_updated['fullstack'] = len(frontend | backend)

print(courses_updated)