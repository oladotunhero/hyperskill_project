def greet(bot_name, created_year ):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {created_year}.")


def remind_name():
    print("Please, remind me your name.")
    # reading a name
    your_name = input()
    print(f"What a great name you have, {your_name}!")

def guessing_game():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    # reading all remainders
    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())
    your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Your age is {your_age}; that's a good time to start programming!")

def count():
    print('Now I will prove to you that I can count to any number you want.')

    number = int(input("Enter a number: \n"))
    for i in range(number + 1):
        print(i, "!")
    print('Completed, have a nice day!')

def test():
    print("Let's test your programming knowledge.")
    question = "Why do we use methods?"
    print(question)
    answers = ["1. To repeat a statement multiple times.",
              "2. To decompose a program into several small subroutines.",
              "3. To determine the execution time of a program.",
              "4. To interrupt the execution of a program."]
    for answer in answers:
        print(answer)

    correct_answer = "2"
    while True:
        user_input = input("Enter a number: ")

        if user_input == correct_answer:
            break
        else:
            print("Please, try again.")

    print('Completed, have a nice day!')

chat_bot_name = input("enter the name of your bot: \n")
chat_bot_year = int(input("Enter the year you created the bot: \n"))

# Now we can use these functions
greet(chat_bot_name, chat_bot_year)
remind_name()
guessing_game()
count()
test()
