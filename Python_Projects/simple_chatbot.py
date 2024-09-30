def greet(bot_name, created_year ):
    print(f"Hello! My name is {bot_name}.\nI was created in {created_year}.")


def remind_name():
    print("Please, remind me your name.")
    # reading a name
    your_name = input()
    print(f"What a great name you have, {your_name}!")


# Now we can use these functions
chat_bot_name = input("enter the name of your bot: \n")
chat_bot_year = int(input("Enter the year you created the bot: \n"))
greet(chat_bot_name, chat_bot_year)
remind_name()

#Age Guessing game
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {your_age}; that's a good time to start programming!")