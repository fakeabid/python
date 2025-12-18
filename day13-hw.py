# Homework Problem:
# A local school wants to keep track of students' names in a file.

# Ask the user how many student names they want to add.

# Then, take that many names as input and store each name on a new line in a file called students.txt.

# If the file already exists, first show all existing names, then add the new ones without removing the old ones.

# After saving the new names, read and display the updated list of all student names.

n = int(input('How many names to add? (Provide a number) '))

try:
    f = open('students.txt', 'r')

except:
    print("creating new file!")
    print("opening students.txt:")
else:
    print("opening students.txt:\n")
    print(f.read())

    f.close()
    
print("---add content:---")
f = open('students.txt', 'a')
for i in range(n):
    name = input()
    f.write(f'{name}\n')

f.close()
f = open('students.txt', 'r')

print('\ndisplaying file:')
print(f.read())

f.close()