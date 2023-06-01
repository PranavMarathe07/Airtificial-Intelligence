import nltk
from nltk.chat import Chat

pairs = [
    [
        "Hi|Hello|Hey",
        ["Hello How may i assist you?", "Hi sir how mayi help you"]
    ],
    [
        "What is your Name?",
        ["Myself PyBot! A chatbot developed using python."]
    ],
    [
        "What is 2+2?",
        ["Answer is: 4"]
    ],
    [
        "pls tell me who will be the winner in ipl final",
        ["it's difficult to predict", "It may be chances that csk may win."]
    ],
    [
        "quit",
        ["Thank you for using my services!!"]
    ],
]

print("Welcome to PyBot!!")
chat = Chat(pairs)
chat.converse()