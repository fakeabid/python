# Write a Python program that does the following:
# Store a short paragraph about a Python course using a multiline string.
# Display the length of the paragraph (number of characters).
# Display the first and last characters in the paragraph.
# Slice and print a short preview: the first 50 characters.
# Replace all occurrences of the word "Python" with "PYTHON" (in all caps).
# Convert the entire paragraph to lowercase.
# Remove any extra whitespaces from the start or end.
# Split the paragraph into individual words and print the list.
# Check if the word "course" exists in the paragraph. Print a message if found.
# Display the final message:
# "The course description is {} characters long and has {} words." using the format() method.

para = '''A warm welcome to the Python Programming course by Uplatz. Python is a high-level, general-purpose and a very popular programming language. Python programming language is being used in web development, Machine Learning applications, along with all cutting edge technology in software industry. Python is a popular programming language. It was created by Guido van Rossum, and released in 1991. It is used in web development, data science, creating software prototypes, and so on. Fortunately for beginners, Python has simple easy-to-use syntax. Python is one of the high-level, interpreted and general-purpose programming languages that is easy to use, comprehensive and powerful.'''

print(len(para))

print(para[0], para[-1])

print(para[:50])

print(para.replace('Python', 'PYTHON'))

print(para.lower())

print(para.strip())

print(para.split())

if "course" in para:
    print('Yes course exists.')

print(f"The course description is {len(para)} characters long and has {len(para.split())} words." )