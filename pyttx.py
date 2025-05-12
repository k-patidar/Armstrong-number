'''import pyttsx3
engine = pyttsx3.init()
engine.say("hi sir i will assist you what kind of halp requair for you i try to resolve it as soon as posibally")
engine.runAndWait() '''


'''import pyttsx3
engine = pyttsx3.init()
engine.say("hi kundan patidar how may i help you:")
engine.runAndWait () '''
'''
import pyttsx3
import os
import sys

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def execute_command(command):
    if "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc")
    elif "shutdown" in command:
        speak("Shutting down the system")
        os.system("shutdown /s /t 10")
    elif "restart" in command:
        speak("Restarting the system")
        os.system("shutdown /r /t 10")
    elif "exit" in command:
        speak("Goodbye!")
        sys.exit()
    else:
        speak("Command not recognized")

def chatbot():
    speak("Hello! I am your personal assistant. How can I help you?")
    while True:
        user_input = input("You: ").lower()
        execute_command(user_input)

if __name__ == "__main__":
    chatbot()'''
import nltk
import random
from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]],
    [r"how are you?", ["I'm an AI, but I'm doing great! How about you?"]],
    [r"what is your name?", ["I'm an AI chatbot. You can call me ChatBot."]],
    [r"bye|goodbye", ["Goodbye! Have a great day!", "See you soon!"]],
    [r"(.*)", ["I'm not sure I understand. Can you rephrase that?", "Tell me more!"]]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start chat
def chat():
    print("ChatBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["bye", "exit", "quit"]:
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

# Run chatbot
if __name__ == "__main__":
    chat()

