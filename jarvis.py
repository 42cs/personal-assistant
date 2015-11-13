import sys
import requests 
import json
import apis

def square(n):
    """ Square numbers  

    >>> square(2)
    4 
    >>> square(3)
    8
    """
    return n**n

def dispatcher(command, arg):
    """ Does things """
    if command == "weather":
        print("Here's the weather forcast for "+arg)
        print(apis.fetch_weather(arg))
    if command == "square":
        print("The square of " + arg + " is " + str(square(int(arg))))
    elif command == "go away":
        print("It sounds like you no longer need my assistance")
        print("Very well. Goodbye!")
        return 
    elif command == "bye":
        print("Goodbye! Have a good day!")
        return
    # Reprompt the user. 
    prompter()


def prompter():
    """ asks for things """

    command = input("How may I help you?: [weather, square, go away, bye]")
    if command == "weather":
        city = input("Sure thing! What city?")
        dispatcher(command, city)
    if command == "square":
        num = input("I love math! What number?")
        dispatcher(command, num)
    elif command == "stocks": # TODO
        pass
    else:
        dispatcher(command, "")

def starter(cliargs):
    # TODO: Finish up command line interface
    print("DEBUG: Called with ", cliargs[1:])

    print("Summoning Jarvis")
    print("Good evening!")

    if (len(cliargs) > 1):
        command = cliargs[2]
        # TODO: Call dispatcher with args instead of prompting user. 
    else:
        prompter()


if __name__ == "__main__":
    starter(sys.argv)
