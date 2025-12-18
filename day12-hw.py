# You are building a simple customer feedback system for a local restaurant. The system should ask users to enter their name and feedback. Your task is to:
# Ask the user to enter their name and feedback.
# If the user leaves the name or feedback empty, display an error message using exception handling.
# If all inputs are valid, print a thank-you message along with the user's name and feedback.
# Use the try, except, and finally blocks to structure your code safely.

while True:
    try:
        name = input('enter your name: ')
        feedback = input('enter a feedback: ')

        if not name.strip() or not feedback.strip():
            raise ValueError('please enter both name and feedback.')      
    except ValueError as e:
        print(e)
        continue
    else:
        print(f'thank you {name}!\nyour feedback: {feedback}')
        break