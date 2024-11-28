import os
import random
import time
from rich.console import Console

console = Console()

class Questions:
    '''Defines the questions'''
    def __init__(self, number, country, capital, incorrect_1, incorrect_2):
        self.number = number
        self.country = country
        self.capital = capital
        self.incorrect_1 = incorrect_1
        self.incorrect_2 = incorrect_2
    
    def display_question(self):
        """displays the question
        
        prints the question, with three possible answers
        the three possible answers are A, B and C
        and we want to assign the capital to one of these answers randomly
        and record which answer is the correct one
        """
        print(f"Question {self.number}: What is the capital of {self.country}?")
        possible_answers = [self.capital, self.incorrect_1, self.incorrect_2]
        random.shuffle(possible_answers)
        print('A: ', possible_answers[0])
        print('B: ', possible_answers[1])
        print('C: ', possible_answers[2])
        return possible_answers


def clear_screen():
    """clears the screen"""
    os.system("cls" if os.name == "nt" else "clear")


def start_game():
    """starts the game"""
    list_of_questions = [
        {
            'country':"the United States", 
            'capital': "Washington DC", 
            'incorrect_1':"Los Angeles", 
            'incorrect_2':"New York",
        },
        {
            'country':"China",
            'capital': "Beijing",
            'incorrect_1':"Hong Kong",
            'incorrect_2':"Shanghai",
        },
        {
            'country':"Japan",
            'capital': "Toyko",
            'incorrect_1':"Hiroshima",
            'incorrect_2':"Osaka",
        },
        {
            'country':"the United Kingdom",
            'capital': "London",
            'incorrect_1':"Birmingham",
            'incorrect_2':"Manchester",
        },
    ]

    score = 0

    for index, question in enumerate(list_of_questions):
        print("Your score is currently:", score)
        question = Questions(
            number=index + 1,
            country=question["country"],
            capital=question["capital"], 
            incorrect_1=question["incorrect_1"], 
            incorrect_2=question["incorrect_2"]
        )
        possible_answers = question.display_question()
        while True:
            question_answer = input("Please select an option of A, B or C, then press Enter:\n")
            if question_answer.upper() not in ['A', 'B', 'C']:
                print("That is not a valid answer. Please try again.")
            else:
                break

        if question_answer.upper() == "A" and possible_answers[0] == question.capital:
            print("Correct")
            score += 1
        elif question_answer.upper() == "B" and possible_answers[1] == question.capital:
            print("Correct")
            score += 1
        elif question_answer.upper() == "C" and possible_answers[2] == question.capital:
            print("Correct")
            score += 1
        else:
            print("Incorrect")
            print("The correct answer is: ", capital)

        time.sleep(2)
        clear_screen()

    print("Game Over")
    print("Your final score is:", score)
    time.sleep(2)
    display_menu()


def display_instructions():
    """displays the instructions"""
    print("Instructions:")
    print("You will be asked a series of questions about capital cities")
    print("You will be given three possible answers, and you must select the correct one")
    print("You will be scored on the number of correct answers you give")
    print("Good luck!")
    print("Press any key to return to the menu")
    input()
    clear_screen()
    display_menu()


def display_menu():
    """displays the menu"""
    print("Welcome to the Capital City Quiz")
    print("Please select an option:")
    print("1. Start Game")
    print("2. Exit")
    print("3. Instructions")
    while True:
        user_input = input("Please select an option by entering a number:\n")
        if user_input == "1":
            clear_screen()
            start_game()
            break
        elif user_input == "2":
            print("Goodbye")
            exit()
        elif user_input == "3":
            clear_screen()
            display_instructions()
        else:
            print("That is not a valid option. Please try again.")

if __name__ == "__main__":
    display_menu()



