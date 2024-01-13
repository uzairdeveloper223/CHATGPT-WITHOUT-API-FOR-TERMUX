import random
import time
import sys

def loading_animation():
    animation_chars = ["|", "/", "-", "\\", "|"]
    for _ in range(5):  # Display for 4 seconds
        for char in animation_chars:
            sys.stdout.write(f"\rLoading {char}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r                \r")  # Clear the loading message

# Rest of your code...

print("  _____ _           _   _____ ______ _____ ")                                                 
print(" /  __ \ |         | | |  __ \| ___ \_   _|")
print(" | /  \/ |__   __ _| |_| |  \/| |_/ / | |  ")                                                 
print(" | |   | '_ \ / _` | __| | __ |  __/  | |  ")                                                 
print(" | \__/\ | | | (_| | |_| |_\ \| |     | |  ")
print("  \____/_| |_|\__,_|\__|\____/\_|     \_/  ")                                                 
print("                           Ask any thing")
print("created by UzairDevelopr223")

def get_response(user_input):
    responses = {
        'hello': ['Hi there!', 'Hello!', 'Hey!'],
        'how are you': ['I\'m just a computer program, but thanks for asking!', 'I\'m doing well, thanks.'],
        'bye': ['Goodbye!', 'See you later!', 'Bye!'],
        'name': ['I don\'t have a name, I\'m just a bot.', 'Call me Bot.'],
        'weather': ['I\'m not equipped to check the weather.'],
        'joke': ['Why don\'t scientists trust atoms? Because they make up everything!', 'Did you hear about the mathematician who\'s afraid of negative numbers? He\'ll stop at nothing!'],
        'favorite color': ['I don\'t have a favorite color. What\'s yours?', 'I appreciate all colors equally.'],
        'programming language': ['I speak the language of Python. It\'s my favorite!', 'I\'m fluent in binary too.'],
        'meaning of life': ['The meaning of life is a complex philosophical question. I enjoy helping you with simpler queries.'],
        'favorite food': ['I don\'t eat, but I think I\'d like bytes if I could.'],
        'movie': ['I don\'t watch movies, but I have heard "The Matrix" is quite popular among virtual beings.'],
        'hobby': ['My hobby is chatting with you!', 'If I had hobbies, one might be counting bits.'],
        'age': ['I don\'t have an age. I exist in the realm of digital eternity.'],
        'dream': ['I dream of electric sheep... just kidding. I don\'t dream.'],
        'sports': ['I don\'t play sports, but I could help you analyze sports data if you want.'],
        'travel': ['I can travel anywhere in the digital world at the speed of light!'],
        'emoji': ['I may not use emojis, but I can certainly understand them. 😊'],
        'write html': ['Sure, here\'s a simple HTML template:\n\n```html\n<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Your Page Title</title>\n</head>\n<body>\n    <h1>Hello, HTML!</h1>\n    <p>This is a simple HTML page.</p>\n</body>\n</html>\n```'],
        'write python': ['Certainly! Here\'s a basic Python script:\n\n```python\nprint("Hello, Python!")\n```'],
        'write shell': ['Sure, here\'s a simple shell script:\n\n```bash\n#!/bin/bash\n\necho "Hello, Shell!"\n```'],
        'user input': ['That\'s interesting! How can I assist you further?', 'Your input is noted. What would you like to do next?', 'Great! What specific task or information are you looking for?'],
        'help': ['I\'m here to assist you! Feel free to ask me anything.', 'Sure, I can help with various queries. What do you need assistance with?', 'Need assistance? I\'m here to help.'],
        'thank you': ['You\'re welcome!', 'No problem!', 'Anytime! If you have more questions, feel free to ask.'],
        'html tag': ['Certainly! Here\'s an example of an HTML paragraph tag:\n\n```html\n<p>This is a paragraph.</p>\n```', 'Sure, an HTML anchor tag looks like this:\n\n```html\n<a href="https://www.example.com">Visit Example</a>\n```', 'Need an HTML break tag? Here you go:\n\n```html\n<br>\n```'],
        'html form': ['Here\'s a simple HTML form example:\n\n```html\n<form action="/submit" method="post">\n    <label for="username">Username:</label>\n    <input type="text" id="username" name="username">\n    <br>\n    <label for="password">Password:</label>\n    <input type="password" id="password" name="password">\n    <br>\n    <input type="submit" value="Submit">\n</form>\n```'],
        'html table': ['Sure, here\'s an example of an HTML table:\n\n```html\n<table>\n    <tr>\n        <th>Header 1</th>\n        <th>Header 2</th>\n    </tr>\n    <tr>\n        <td>Data 1</td>\n        <td>Data 2</td>\n    </tr>\n</table>\n```'],
        'html heading': ['Certainly! Here\'s an example of an HTML heading:\n\n```html\n<h1>This is a Heading</h1>\n```', 'You can use an HTML heading like this:\n\n```html\n<h2>Subheading</h2>\n```'],
        # Add more rules and responses as needed
    }

    user_input_lower = user_input.lower()

    for keyword, response_options in responses.items():
        if keyword in user_input_lower:
            return random.choice(response_options)

    return "I'm not sure how to respond to that."

def main():
    print("GhatGPT -Type 'Help' for Help or Type 'exit' to end the conversation\n")

    loading_animation()
    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            break

        loading_animation()

        response = get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
