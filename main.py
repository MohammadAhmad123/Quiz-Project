# Function to display the welcome message
def welcome_message():
    print("Welcome to the Python Quiz!")
    print("Answer the questions by selecting the correct option (1-4).")

# Function to display a question and its options
def display_question(question, options):
    print("\n" + question)  # Print the question
    for i, option in enumerate(options, 1):  # Loop through the options and number them
        print(f"{i}. {option}")  # Display each option with its corresponding number
    return get_user_input(len(options))  # Call the input function and return the user's choice

# Function to get and validate user input
def get_user_input(num_choices):
    while True:  # Keep prompting until valid input is provided
        try:
            user_choice = int(input("Enter your answer (1-4): "))  # Get user input and convert to integer
            if 1 <= user_choice <= num_choices:  # Check if input is within valid range
                return user_choice  # Return valid input
            else:
                print("Invalid choice. Please select a number between 1 and 4.")  # Error message for out-of-range input
        except ValueError:  # Handle non-integer inputs
            print("Invalid input. Please enter a number.")  # Error message for invalid input

# Function to ask questions and calculate the score
def calculate_score(questions, correct_answers):
    score = 0  # Initialize score counter
    for idx, (q, opts) in enumerate(questions):  # Loop through each question
        user_answer = display_question(q, opts)  # Display question and get user answer
        if user_answer == correct_answers[idx]:  # Compare user answer with the correct one
            score += 1  # Increment score if the answer is correct
    return score  # Return the final score

# Function to display the final score and feedback
def display_results(score, total):
    print(f"\nYour total score is: {score}/{total}")  # Display the user's score
    # Provide feedback based on performance
    if score == total:
        print("Excellent! You got all the answers correct.")  # Perfect score message
    elif score >= total / 2:
        print("Good job! You passed the quiz.")  # Pass message
    else:
        print("Keep practicing. Better luck next time!")  # Encourage improvement

# Function to display a thank you message
def thank_you_message():
    print("\nThank you for taking the quiz!")  # Farewell message

# Main program execution starts here
if __name__ == "__main__":
    # List of questions with their respective options
    questions = [
        ("What is the capital of England?", ["Berlin", "Madrid", "London", "Rome"]),
        ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"]),
        ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Shark"]),
        ("what is the longest running animated TV show'?", ["The Family Guy", "The simpsons", "Arthur", "South Park"]),
        ("What is the chemical symbol for gold?", ["AU", "CO2", "O2", "HE"]),
        ("Which country is famous for the Great Wall?", ["India", "China", "Egypt", "Mexico"]),
        ("what other languages are spoken in Saudi Arabia?", ["Spanish", "Urdu", "French", "English"]),
        ("Which gas do plants absorb from the atmosphere?", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"]),
        ("what is the most popular browser?", ["Oprea GX", "Brave", "Firefox", "Chrome"]),
        ("what is the most popular social media website?", ["YouTube", "Facebook", "Wikipedia", "Twitter"]),
    ]

    correct_answers = [3, 2, 2, 2, 1, 2, 2, 3, 4, 1]  # Correct answers (1-based indexing)

    welcome_message()  # Call the welcome function
    score = calculate_score(questions, correct_answers)  # Calculate the user's score
    display_results(score, len(questions))  # Display the quiz results
    thank_you_message()  # Show the thank you message
